from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import Union

# Custom Exception Classes
class ItemNotFoundException(HTTPException):
    def __init__(self, detail: str = "Item not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
        
# Exception Handlers
async def item_not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.detail},
    )