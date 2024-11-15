from enum import Enum
from pydantic import AnyUrl, BaseModel, EmailStr, Field


class RedisAuthModel(BaseModel):
    session_id: str

class MusicBand(str, Enum):
   AEROSMITH = "AEROSMITH"
   QUEEN = "QUEEN"
   ACDC = "AC/DC"
   
class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=128)
    username: str = Field(min_length=1, max_length=128, pattern="^[A-Za-z0-9-_]+$")
    email: EmailStr
    age: int = Field(ge=18, default=None)  # must be greater or equal to 18
    favorite_band: MusicBand | None = None  # only "AEROSMITH", "QUEEN", "AC/DC" values are allowed to be inputted
    website: AnyUrl | None = None