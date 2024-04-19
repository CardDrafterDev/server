# collecting all routers into ones

from fastapi import APIRouter
from .createRouter import create_router
from .readRouter import read_router
from .updateRouter import update_router


Router = APIRouter()
Router.include_router(create_router)
Router.include_router(read_router)
Router.include_router(update_router)