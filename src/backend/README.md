# Backend Telegram Mini App

FastAPI, aiogram, Tortoise ORM, Aerich и PostgreSQL. Полная инструкция по настройке БД, окружения, HTTPS и запуску находится в [корневом README](../../README.md).

Из этого каталога после заполнения `.env` и создания PostgreSQL-базы:

```sh
uv sync
uv run -m aerich init-db
uv run python -m src
```

`init-db` используется для новой базы. Для существующей базы после получения миграций выполните `uv run -m aerich upgrade`. Конфигурация Aerich уже включена в `pyproject.toml`.

После изменения моделей:

```sh
uv run -m aerich migrate --name describe_change
uv run -m aerich upgrade
```

Сохраняйте миграции в Git. Перед изменениями рабочей БД сделайте резервную копию. Backend регистрирует Telegram webhook при запуске, поэтому `API_URL` должен быть доступным HTTPS-адресом.
