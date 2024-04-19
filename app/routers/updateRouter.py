import app.database.database as db

from . import dataModels as models
from app.errorHandling.errorHandler import DBErrorHandler

from fastapi import APIRouter
from fastapi import status, Response




update_router = APIRouter()
dbhandler = DBErrorHandler(__name__)


@update_router.put("/update_collection")
async def update_user_collection(user: models.User, response: Response):
    try:
        db.update_user_collection(user_id=user.user_id, collection=user.collection)
        response.status_code = status.HTTP_202_ACCEPTED

    except Exception as e:
        dbhandler.handle_misc(f"Couldn't update collection: {e}")



@update_router.put("/update_inventory")
async def update_user_inventory(user: models.User, response: Response):
    try:
        db.update_user_inventory(user_id=user.user_id, collection=user.inventory)
        response.status_code = status.HTTP_202_ACCEPTED

    except Exception as e:
        dbhandler.handle_misc(f"Couldn't update inventory: {e}")
