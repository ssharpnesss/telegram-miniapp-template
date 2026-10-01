# Frontend Telegram Mini App

React, TypeScript, Vite и Telegram SDK. Полная инструкция по настройке бота, HTTPS, backend и базы данных находится в [корневом README](../../../README.md).

Команды из этого каталога:

```sh
npm ci
npm run dev
npm run build
```

Скопируйте `.env.example` в `.env`, задайте `VITE_BASE_API_URL` (HTTPS-адрес backend без `/api/v1`) и замените домен в `server.allowedHosts` в `vite.config.ts` на домен своего frontend-туннеля. После изменения `.env` перезапустите Vite; для публикации выполните новую сборку.

Открывайте приложение через Telegram-бота для получения init data. Результат production-сборки находится в `dist`.
