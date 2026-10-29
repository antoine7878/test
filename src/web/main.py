from fastapi import APIRouter

from src.web.routes import home, login

web_router = APIRouter()
web_router.include_router(home.router)
web_router.include_router(login.router)
