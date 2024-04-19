import app.database.database as db

from . import dataModels as models


from fastapi import APIRouter
from fastapi import status, Response




update_router = APIRouter()


@update_router.put("/update_collection")
async def update_user_collection(user: models.User, response: Response):

    db.update_user_collection(user_id=user.user_id, collection=user.collection)

    response.status_code = status.HTTP_202_ACCEPTED

@update_router.put("/update_inventory")
async def update_user_inventory(user: models.User, response: Response) -> None:
    
    db.update_user_inventory(user_id=user.user_id, inventory=user.inventory)


    response.status_code = status.HTTP_202_ACCEPTED