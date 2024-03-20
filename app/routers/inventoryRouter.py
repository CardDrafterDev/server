from fastapi import APIRouter, HTTPException
import app.errorHandling.errorHandler as error
import app.database.database as db

inventory_router = APIRouter()



@inventory_router.get("/inventory/get/{user_id}")
async def get_user_inventory(user_id):
    if not user_id:
        error.handle_http_err(404, "User ID does not exist")

    try:
        user_id = int(user_id)
    except ValueError:
        error.handle_http_err(400, "User ID is not an integer")

    user_inventory = db.get_user_inventory(user_id)
    return user_inventory
