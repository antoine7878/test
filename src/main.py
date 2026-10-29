from pathlib import Path

import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from src.api.main import api_router
from src.core.config import settings
from src.core.db import engine
from src.web.admin import ItemAdmin, UserAdmin
from src.web.main import web_router

STATIC_DIR = Path(__file__).parent / "web" / "static"


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.FASTAPI_ENV != "development":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(web_router)

admin = Admin(app, engine)

admin.add_view(UserAdmin)
admin.add_view(ItemAdmin)
