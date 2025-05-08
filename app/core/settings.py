from pydantic_settings import BaseSettings

from app.core.constants import Environment


class Settings(BaseSettings):
    api_name: str = "Age Group API"
    api_version: str = "1.0.0"
    api_host: str = "0.0.0.0"
    api_port: int
    prefix: str = "/api"

    mongo_host: str
    mongo_port: int
    database_name: str

    environment: str = Environment.LOCAL
