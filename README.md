# Telegram Mini App Template

Starter repository for a Telegram Mini App with a React + TypeScript frontend and a Python backend using FastAPI, aiogram, and PostgreSQL.

## What's included

- `src/client/app` — Vite, React, and TypeScript app.
- `src/backend` — FastAPI app, Telegram bot, and PostgreSQL integration.
- `src/backend/.env.example` — names of the backend settings to configure.

## Requirements

- Node.js 20.19+ or 22.12+ and npm.
- Python 3.12+ and [uv](https://docs.astral.sh/uv/).
- A PostgreSQL database and a Telegram bot token from [@BotFather](https://t.me/BotFather).

## Run locally

1. Copy `src/backend/.env.example` to `src/backend/.env` and fill in your local values. Keep `.env` private.
2. Start the backend:

   ```powershell
   cd src/backend
   uv sync --no-install-project
   uv run python -m src
   ```

3. In another terminal, start the frontend:

   ```powershell
   cd src/client/app
   npm ci
   npm run dev
   ```

The backend registers a Telegram webhook during startup, so `API_URL` must point to a publicly reachable HTTPS endpoint. For local development, expose the backend through a tunneling service and set `API_URL` to its HTTPS URL. Set `MINIAPP_URL` to the frontend URL where your Mini App is hosted.

## Use this repository as a GitHub template

On GitHub, open **Settings → General**, enable **Template repository**, then use the **Use this template** button to create a separate repository for each project. New repositories start from the template's current default branch and do not inherit its commit history.

## License

MIT. See [LICENSE](LICENSE).
