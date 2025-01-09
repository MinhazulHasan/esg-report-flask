from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PERPLEXITY_API_KEY: str
    DRIVER: str
    SERVER_NAME: str
    DATABASE_NAME: str
    TRUSTED_CONNECTION: str

    class Config:
        env_file = ".env"

config = Settings()