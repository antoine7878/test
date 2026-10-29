from datetime import UTC, datetime

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from src.web.templating import templates

router = APIRouter(tags=["home"], include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "index.html")


@router.get("/partials/time", response_class=HTMLResponse)
async def current_time(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "partials/time.html", {"now": datetime.now(UTC)})
