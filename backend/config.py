from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool
    ENV: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
