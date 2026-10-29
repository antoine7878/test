from typing import Any

from sqladmin import ModelView
from sqlalchemy.orm import InstrumentedAttribute

from src.models import Item, User


def cols(*attrs: Any) -> list[InstrumentedAttribute[Any]]:
    return list(attrs)


def col(attr: Any) -> InstrumentedAttribute[Any]:
    return attr


class UserAdmin(ModelView, model=User):
    column_list = cols(User.email, User.is_active, User.is_superuser, User.created_at)


class ItemAdmin(ModelView, model=Item):
    column_list = cols(Item.id, Item.title, Item.created_at, Item.owner)
    column_formatters = {col(Item.owner): lambda m, _: m.owner.email if m.owner else ""}
    column_formatters_detail = column_formatters
