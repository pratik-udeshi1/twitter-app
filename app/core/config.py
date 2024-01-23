import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Twitter Clone"
    database_url: str = os.getenv("DATABASE_URL", None)
    secret_key: str = os.getenv("SECRET_KEY", None)
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    SettingsConfigDict(env_file='.env')


settings = Settings()
