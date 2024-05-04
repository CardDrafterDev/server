import app.database.database as db
import app.errorHandling.errorHandler as error

import app.models.dataModels as models 


from fastapi import APIRouter
from fastapi import Response, status



http_handler = error.HttpErrorHandler(__name__)
db_handler = error.DBErrorHandler(__name__)

create_router = APIRouter()


@create_router.post("/create_user")
async def create_user(user: models.User, response: Response) -> None:
    user_id = user.user_id
    if not user_id:
        error.handle_http_err(file_name=__name__, status=404, msg="User ID does not exist")

    try:
        user_id = int(user_id)
    except ValueError:
        error.handle_http_err(file_name=__name__, status=400, msg="User ID is not an integer")
        

    db.create_user(user_id)
    response.status_code = status.HTTP_201_CREATED
    