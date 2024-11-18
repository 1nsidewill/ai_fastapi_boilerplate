from fastapi import APIRouter
from src.exceptions import *

crud_router = APIRouter()

@crud_router.api_route("/get_age", methods=["GET"])
async def get_age(name: str):
    """
    ## Description:
    - 이름을 넣으면 나이를 알려줍니다.
    """
    
    if name == "Will":
        print("29")
        return {"age" : "29"}
    else:
        raise ItemNotFoundException(detail=f"No age information found for name: {name}")