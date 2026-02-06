from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="COOKMATE_", env_file=".env", extra="ignore")

    cors_allow_origins: str = "*"
    database_url: str = "postgresql+psycopg://cookmate:cookmate@localhost:5432/cookmate"

    class config:
        env_file =".env"

settings = Settings()
