from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Union

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Custom Exception Classes
class ItemNotFoundException(HTTPException):
    def __init__(self, detail: str = "Item not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
        
class ExistsException(HTTPException):
    def __init__(self, detail: str = "Item already exists"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

# Exception Handlers
async def item_not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    if request.method == "GET":
        # Render an error page for GET requests
        return templates.TemplateResponse(
            "error.html", 
            {"request": request, "message": exc.detail, "status_code": exc.status_code}, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    else:
        # Return JSON response for other request methods
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": exc.detail},
        )

async def exists_exception_handler(request: Request, exc: ExistsException):
    if request.method == "GET":
        return templates.TemplateResponse(
            "error.html", 
            {"request": request, "message": exc.detail, "status_code": exc.status_code}, 
            status_code=status.HTTP_400_BAD_REQUEST
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": exc.detail},
        )