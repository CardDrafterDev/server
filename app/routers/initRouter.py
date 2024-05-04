# collecting all routers into one

from fastapi import APIRouter
from .createRouter import create_router
from .readRouter import read_router
from .updateRouter import update_router
from .adminRouter import admin_router


Router = APIRouter()
Router.include_router(create_router)
Router.include_router(read_router)
Router.include_router(update_router)
Router.include_router(admin_router, include_in_schema=False)
