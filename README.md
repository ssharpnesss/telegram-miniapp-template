# Шаблон Telegram Mini App

Стартовый шаблон Telegram Mini App: фронтенд на React и TypeScript, бэкенд на Python с FastAPI, aiogram и PostgreSQL.

## Что входит в шаблон

- `src/client/app` — приложение на Vite, React и TypeScript.
- `src/backend` — приложение на FastAPI, Telegram-бот и интеграция с PostgreSQL.
- `src/backend/.env.example` — пример настроек бэкенда.

## Требования

- Node.js 20.19+ или 22.12+ и npm.
- Python 3.12+ и [uv](https://docs.astral.sh/uv/).
- База данных PostgreSQL и токен Telegram-бота, созданного через [@BotFather](https://t.me/BotFather).

## Локальный запуск

1. Скопируйте `src/backend/.env.example` в `src/backend/.env` и укажите свои настройки. Не публикуйте файл `.env`.
2. Запустите бэкенд:

   ```powershell
   cd src/backend
   uv sync --no-install-project
   uv run python -m src
   ```

3. В другом терминале запустите фронтенд:

   ```powershell
   cd src/client/app
   npm ci
   npm run dev
   ```

При запуске бэкенд регистрирует webhook в Telegram, поэтому `API_URL` должен указывать на доступный из интернета HTTPS-адрес. Для локальной разработки откройте доступ к бэкенду через туннель и укажите его HTTPS-адрес в `API_URL`. В `MINIAPP_URL` укажите адрес размещённого фронтенда Mini App.

## Как использовать репозиторий как шаблон GitHub

На GitHub откройте **Settings → General** и включите **Template repository**. После этого нажмите **Use this template**, чтобы создать отдельный репозиторий для нового проекта. Новый репозиторий будет содержать файлы текущей основной ветки шаблона, но не его историю коммитов.

## Лицензия

MIT. Текст лицензии находится в файле [LICENSE](LICENSE).
