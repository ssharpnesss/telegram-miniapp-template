from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from fastapi import FastAPI

from src.core.utils.startup import lifespan

ROOT_DIR = Path(__file__).resolve().parents[2]

class Config(BaseSettings):
    BOT_TOKEN: SecretStr

    POSTGRES_USER: SecretStr
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: SecretStr
    POSTGRES_HOST: SecretStr
    POSTGRES_PORT: SecretStr

    MINIAPP_URL: str = "https://"
    API_URL: str = "https://"

    APP_HOST: str = "localhost"
    APP_PORT: int = 8080

    @property
    def db_url(self) -> str:
        return (
            "asyncpg://"
            f"{self.POSTGRES_USER.get_secret_value():{self.POSTGRES_PASSWORD.get_secret_value()}}"
            f"@{self.POSTGRES_HOST.get_secret_value():{self.POSTGRES_PORT.get_secret_value()}}"
            f"/{self.POSTGRES_DB.get_secret_value()}"
        )

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8"
    )


config = Config()
bot = Bot(
    token=config.BOT_TOKEN.get_secret_value(),
    default=DefaultBotProperties(parse_mode="HTML")
)
dp = Dispatcher()

app = FastAPI(lifespan=lifespan)

TORTOISE_ORM = {
    "connections": {
        "default": config.db_url,
    },
    "apps": {
        "models": {
            "models": ["src.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}