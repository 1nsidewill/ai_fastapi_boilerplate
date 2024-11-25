from fastapi import APIRouter, Request
from src.auth import repository
from src.config import get_settings

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


auth_router = APIRouter()

# Load Env
config = get_settings()

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@auth_router.api_route("/hello_world", methods=["POST"])
async def hello_world(item: repository.RedisAuthModel):
    """
    ## Description:
    - Redis에 Sessin_id가 있으면 Hello world, 없으면 Not There 을 반환합니다.
    
    ## Parameters:
    - `item` (RedisAuthModel): Redis에 필요한 정보를 담는 Model입니다.
    - **session_id**: Redis에 사용하는 session_id 입니다.

    ## Returns:
    - `result`: 결과입니다
    """
    print(item.session_id)
    
    return {"result" : "Not There"}

@auth_router.api_route("/what_is_in_env", methods=["GET"])
async def what_is_in_env():
    """
    ## Description:
    - Env File의 내용을 불러옵니다
    """
    print(config.MILVUS_URL)
    
    return {"result" : config.MILVUS_URL}

# Home route to render the template
@auth_router.api_route("/index", methods=["GET"], response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Renders the index.html template.
    """
    # Sample data to pass to the template
    data = {"title": "Welcome to AI_FASTAPI_BOILERPLATE", "message": "Hello, FastAPI with Templates!"}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})