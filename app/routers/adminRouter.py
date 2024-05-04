from app.auth import admin_handler
import app.models.dataModels as models 

from typing_extensions import Annotated


from fastapi import APIRouter
from fastapi import Request
from fastapi import Depends


admin_router = APIRouter()


@admin_router.get("/admin")
async def admin_panel(request: Request):
    ...