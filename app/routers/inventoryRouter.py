from fastapi import APIRouter, HTTPException
import app.errorHandling.errorHandler as error
import app.database.database as db

inventory_router = APIRouter()



@inventory_router.get("/inventory/get")
async def get_user_inventory(user_id: int):
    try:
        user_id = int(user_id)
    except ValueError:
        error.handle_http_err(file_name=__name__, status=400, msg="User ID is not an integer")

    user_inventory = db.get_user_inventory(user_id)
    if user_inventory:
        return user_inventory
    
    else:
        error.handle_http_err(file_name=__name__, status=404, msg="User inventory not found")
