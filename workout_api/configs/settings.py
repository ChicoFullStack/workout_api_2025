from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:f92032832@31.97.131.128:5432/workout')


settings = Settings()