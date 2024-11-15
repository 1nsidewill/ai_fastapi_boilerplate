from fastapi import FastAPI
from fastapi.responses import RedirectResponse 
from src.config import get_settings

from src.auth.router import auth_router
from src.crud.router import crud_router 

from src.exceptions import *
from src.middleware import *

# Load Env
config = get_settings()

# Initiate app
app = FastAPI(title=config.app_name)

# Show Docs In Main Page
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

# Including Routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(crud_router, prefix="/crud", tags=["crud"])

# Register Middleware
# 세션 같은 경우엔 Middleware을 사용해도 되고 depends 를 사용해도 됨.
app.add_middleware(SessionMiddleware, secret_key=config.secret_key)

# Register custom exception handlers
app.add_exception_handler(ItemNotFoundException, item_not_found_exception_handler)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, proxy_headers=True, forwarded_allow_ips="*")