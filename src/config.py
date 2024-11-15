from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    app_name: str
    
    # Milvus Connection Info
    MILVUS_URL: str
    
    # OpenAPI Connection Info
    OPENAI_API_KEY: str
    
    
    
    
    
    # Select the environment file dynamically based on an environment variable
    model_config = SettingsConfigDict(
        env_file=os.path.join(
            "env", 
            f"{os.getenv('ENVIRONMENT', 'development')}.env"
        ), 
        env_file_encoding='utf-8'
    )
    
@lru_cache
def get_settings():
    return Settings()