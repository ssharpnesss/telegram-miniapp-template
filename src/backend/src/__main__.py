from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.api import setup_routers
from src.bot.handlers import setup_user_handlers

from src.core.config import config, app, dp

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(setup_routers())
dp.include_router(setup_user_handlers())

if __name__ == "__main__":
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT)