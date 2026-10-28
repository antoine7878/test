from datetime import UTC, datetime

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from src.web.templating import templates

router = APIRouter(tags=["web"], include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "index.html")


@router.get("/partials/time", response_class=HTMLResponse)
def current_time(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request, "partials/time.html", {"now": datetime.now(UTC)}
    )
