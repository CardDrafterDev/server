# collecting all routers into ones

from fastapi import APIRouter
from .inventoryRouter import inventory_router
from .collectionRouter import collection_router


Router = APIRouter()
Router.include_router(inventory_router)
Router.include_router(collection_router)
