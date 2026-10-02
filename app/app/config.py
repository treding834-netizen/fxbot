python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_ENV: str = "development"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DATABASE_URL: str = "sqlite:///./fxbot.db"
    SECRET_KEY: str = "insecure-dev-key"
    DEFAULT_MODE: str = "demo"
    BROKER_ADAPTER: str = "demo"

    BROKER_API_KEY: str = ""
    BROKER_API_SECRET: str = ""
    BROKER_ACCOUNT_ID: str = ""
    BROKER_BASE_URL: str = ""


settings = Settings()
