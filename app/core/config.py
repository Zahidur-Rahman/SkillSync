from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    PROJECT_NAME: str = "SkillSync"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
