from app.auth import admin_handler


from fastapi import APIRouter
from fastapi import Request


admin_router = APIRouter()


@admin_router.get("/admin")
async def admin_panel(request: Request):
    ...