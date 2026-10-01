# Шаблон Telegram Mini App

React и TypeScript на фронтенде; FastAPI, aiogram, Tortoise ORM, Aerich и PostgreSQL на бэкенде. Пользователь авторизуется через Telegram init data, а приложение получает его данные из БД через API.

![Telegram](https://img.shields.io/badge/Telegram-Mini_App-26A5E4?logo=telegram&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-3.x-2CA5E0?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.x-009688?logo=fastapi&logoColor=white)

## Структура

- `src/client/app` — frontend на Vite и Telegram SDK.
- `src/backend/src` — API, бот и модели БД.
- `src/backend/src/db/migrations` — миграции Aerich.
- `.env.example` в каталогах backend и frontend — примеры настроек.

## Требования

- Node.js 20.19+ (ветка 20) или 22.12+ и npm.
- Python 3.12+ и [uv](https://docs.astral.sh/uv/getting-started/installation/).
- Запущенный PostgreSQL, клиент `psql` или pgAdmin.
- Бот, созданный через [@BotFather](https://t.me/BotFather).
- Два публичных HTTPS-адреса: для frontend и backend. Для разработки подойдут ngrok или другие HTTPS-туннели.

Примеры копирования файлов ниже используют PowerShell; в Linux/macOS замените `Copy-Item` на `cp`.

## 1. Установка

Создайте репозиторий через **Use this template** или клонируйте этот:

```sh
git clone https://github.com/ssharpnesss/telegram-miniapp-template.git
cd telegram-miniapp-template
```

Из корня установите backend:

```sh
cd src/backend
uv sync
cd ../..
```

Установите frontend:

```sh
cd src/client/app
npm ci
cd ../../..
```

## 2. Создание PostgreSQL-базы

Подключитесь под администратором:

```sh
psql -U postgres -h localhost
```

Выполните SQL, заменив пароль:

```sql
CREATE USER miniapp_user WITH PASSWORD 'replace_with_your_password';
CREATE DATABASE telegram_miniapp OWNER miniapp_user;
```

Выйдите командой `\q`. Можно выполнить SQL в pgAdmin. Здесь создаётся пустая база; таблицы создаст Aerich.

## 3. Окружение и HTTPS

Из корня скопируйте настройки:

```powershell
cp src/backend/.env.example src/backend/.env
cp src/client/app/.env.example src/client/app/.env
```

Настройте HTTPS-туннели к frontend на порту `5173` и backend на `8080`. Если аккаунт ngrok поддерживает два одновременных туннеля, запустите в отдельных терминалах:

```sh
ngrok http 5173
```

```sh
ngrok http 8080
```

При ограничении количества туннелей используйте другой сервис или разместите одну из частей на сервере. Оставьте туннели работающими.

Заполните `src/backend/.env`:

```dotenv
BOT_TOKEN=your_bot_token_from_botfather
POSTGRES_USER=miniapp_user
POSTGRES_PASSWORD=replace_with_your_password
POSTGRES_DB=telegram_miniapp
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

`MINIAPP_URL` — адрес frontend, `API_URL` — адрес backend без `/webhook` и завершающего `/`. Backend сам добавляет путь webhook. Обязательно задайте собственные адреса в `.config`

Текущий код вставляет логин и пароль напрямую в URL БД. Если они содержат символы URL (`@`, `:`, `/`, `#`, `%`), потребуется корректное кодирование при сборке URL. Для первого запуска используйте пароль без этих символов.

В `src/client/app/.env` укажите backend без `/api/v1` и завершающего `/`:

```dotenv
VITE_BASE_API_URL=https://your-backend.example.com
```

В `src/client/app/vite.config.ts` замените существующий домен в `server.allowedHosts` на домен своего frontend-туннеля **без `https://`**. Например:

```ts
server: {
  port: 5173,
  strictPort: true,
  allowedHosts: ["your-frontend.example.com"],
}
```

При смене адресов обновите оба `.env`, `allowedHosts` и адрес Mini App в BotFather, если он настроен. Перезапустите frontend и backend. Файлы `.env` не коммитьте. Переменные `VITE_*` публичны: не помещайте туда токен бота или пароль БД.

## 4. Таблицы и миграции

Все команды Aerich выполняются из `src/backend`. PostgreSQL должен быть запущен, а `.env` заполнен, включая действительный токен бота: конфигурация импортируется и при работе с миграциями.

Для новой пустой БД:

```sh
cd src/backend
uv run -m aerich init-db
```

Конфигурация Aerich уже есть в `pyproject.toml`; повторять `aerich init` не нужно. Используемая версия Aerich применяет существующие миграции к новой базе через `init-db`; если файлов нет, создаёт начальную миграцию и таблицы. Выполняйте команду один раз для новой базы, а не при каждом запуске. Backend не создаёт таблицы автоматически.

Проверка таблиц:

```sh
psql -h localhost -U miniapp_user -d telegram_miniapp -c "\dt"
```

Должны появиться `users` и `aerich`.

### Изменение моделей

После изменений в `src/db/models`:

```sh
uv run -m aerich migrate --name add_user_field
uv run -m aerich upgrade
```

Коммитьте файлы `src/db/migrations` вместе с изменениями моделей. После получения новых миграций из Git на уже инициализированной БД выполняйте только:

```sh
uv run -m aerich upgrade
```

История и неприменённые миграции:

```sh
uv run -m aerich history
uv run -m aerich heads
```

Откат последней миграции:

```sh
uv run -m aerich downgrade
```

Перед изменением или откатом рабочей БД сделайте резервную копию и проверьте SQL: удаление полей может уничтожить данные. Начальная миграция может иметь пустой откат, поэтому `downgrade` не служит способом очистки базы. Не удаляйте историю миграций для исправления существующей БД.

## 5. Запуск

Из `src/backend`:

```sh
uv run python -m src
```

Backend регистрирует webhook `${API_URL}/webhook` и подключает ORM. По умолчанию порт — `8080`, Swagger доступен по `${API_URL}/docs`.

В другом терминале из `src/client/app`:

```sh
npm run dev
```

Оба процесса и туннели должны оставаться запущенными. Отправьте `/start` боту в личном чате и нажмите кнопку открытия Mini App. Для этой кнопки отдельная настройка меню в BotFather не обязательна. При желании настройте Menu Button или Main Mini App, указав HTTPS-адрес frontend.

Открывайте приложение **из Telegram**: API проверяет подписанные init data. Обычная ссылка в браузере без Telegram-контекста не авторизует пользователя. Главная страница показывает `@username`, а если его нет — имя из БД.

## Частые ошибки

| Симптом | Что проверить |
| --- | --- |
| БД недоступна или нет таблицы `users` | PostgreSQL, параметры `.env`, выполнение `init-db` для этой базы. |
| `401` от `/api/v1/users/me` | Открытие из Telegram и токен именно того бота, через которого запущено приложение. |
| `404` от API | URL backend без `/api/v1`; запуск через `uv run python -m src`, подключающий маршруты. |
| `502` от туннеля | Запущен ли backend и совпадает ли порт туннеля. |
| Только `OPTIONS` в логе | Ответ CORS в Network, доступность туннеля, предупреждение ngrok. Клиент уже отправляет `ngrok-skip-browser-warning`. |
| Vite: `Blocked request` | Домен frontend в `server.allowedHosts`. |
| Старый адрес после изменения `.env` | Перезапуск процессов; для production frontend нужна новая сборка. |

## Размещение на сервере

Из `src/client/app`:

```sh
npm run build
```

Разместите `dist` на статическом HTTPS-хостинге. Для клиентских маршрутов настройте fallback на `index.html`. Vite dev server предназначен для разработки.

Для backend установите зависимости через `uv sync`, заполните `.env`, подготовьте PostgreSQL и примените миграции (`init-db` для новой БД, `upgrade` для существующей). Запускайте `uv run python -m src` под менеджером процессов за HTTPS reverse proxy. Укажите постоянные HTTPS-адреса.

Один бот использует один webhook: запуск локальной копии с тем же токеном заменит webhook сервера. Для разработки используйте отдельного бота. Текущий startup сбрасывает ожидающие обновления Telegram (`drop_pending_updates=True`). Перед публичным запуском ограничьте CORS доменом frontend в `src/backend/src/__main__.py`, настройте резервные копии БД и хранение секретов. Автоматическое развёртывание и обслуживание сервера в шаблон не включены.

## Использование как шаблона GitHub

В **Settings → General** включите **Template repository**. **Use this template** создаст новый репозиторий с файлами основной ветки без истории коммитов. Перед публикацией добавьте актуальные файлы миграций в Git, чтобы следующие проекты получали ту же схему БД.

## Источник

Шаблон создан по [обучающему видео Fsoky](https://youtu.be/zgkGAkaQkNc).

## Лицензия

MIT. См. [LICENSE](LICENSE).
