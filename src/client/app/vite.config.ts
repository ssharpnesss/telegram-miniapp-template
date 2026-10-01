import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {allowedHosts: ["c443-31-56-185-188.ngrok-free.app"]}
})
