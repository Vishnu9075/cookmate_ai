from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="COOKMATE_", env_file=".env", extra="ignore")

    # For later: OPENAI_API_KEY, BEDROCK creds, etc.
    environment: str = "dev"
    cors_allow_origins: str = "http://localhost:5173"

settings = Settings()
