from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os

from src.auth.router import auth_router
from src.crud.router import crud_router 

from src.exceptions import *
from src.middleware import *

# Load Env
from src.config import get_settings
config = get_settings()

# Import the database to ensure tables are created
import src.database

# Determine the environment
environment = os.getenv('ENVIRONMENT', 'dev')

# Initiate app with conditional documentation
if environment == 'dev':
    app = FastAPI(title=config.app_name)
else:
    app = FastAPI(title=config.app_name, docs_url=None, redoc_url=None, openapi_url=None)

# Show Docs In Main Page only in development environment
@app.get("/", include_in_schema=False)
async def root():
    if environment == 'dev':
        # Redirect to docs in development environment
        return RedirectResponse(url="/docs")
    else:
        # In other environments, do not show docs
        return {"message": "Welcome to the API. Documentation is not available in this environment."}

# Including Routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(crud_router, prefix="/crud", tags=["crud"])

# Register Middleware
# 세션 같은 경우엔 Middleware을 사용해도 되고 depends 를 사용해도 됨.
app.add_middleware(SessionMiddleware, secret_key=config.secret_key)

# Register custom exception handlers
app.add_exception_handler(ItemNotFoundException, item_not_found_exception_handler)
app.add_exception_handler(ExistsException, exists_exception_handler)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, proxy_headers=True, forwarded_allow_ips="*")