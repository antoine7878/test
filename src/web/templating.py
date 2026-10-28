from pathlib import Path
from typing import Any

from fastapi import Request
from fastapi.templating import Jinja2Templates

from src.core.config import settings

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"


def _site_context(_request: Request) -> dict[str, Any]:
    return {"project_name": settings.PROJECT_NAME}


templates = Jinja2Templates(directory=TEMPLATES_DIR, context_processors=[_site_context])


def is_htmx(request: Request) -> bool:
    return request.headers.get("HX-Request") == "true"
