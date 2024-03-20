from fastapi import APIRouter, HTTPException
import app.errorHandling.errorHandler as error
import app.database.database as db



collection_router = APIRouter()


@collection_router.get("/collection/get/{user_id}")
def get_collection_by_id(user_id):
    if not user_id:
        error.handle_http_err(404, "User ID does not exist")

    try:
        user_id = int(user_id)
    except ValueError:
        error.handle_http_err(400, "User ID is not an integer")
        
    user_collection = db.get_user_collection(user_id)
    if user_collection:
        return user_collection
    
    else:
        error.handle_http_err(404, "User collection not found")

