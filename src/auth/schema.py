from pydantic import BaseModel

class RedisAuthModel(BaseModel):
    session_id: str