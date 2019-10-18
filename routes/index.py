""" Index Resource """
from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from core.config import STATIC_ROOT

templates = Jinja2Templates(directory=STATIC_ROOT)

router = APIRouter()


@router.get("/")
async def index(request: Request):
    """ Angular entrypoint """
    return templates.TemplateResponse("index.html", {"request": request})
