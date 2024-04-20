from fastapi import APIRouter
import app.errorHandling.errorHandler as error
import app.database.database as db


read_router = APIRouter()


http_handler = error.HttpErrorHandler(__name__)
db_handler = error.DBErrorHandler(__name__)


@read_router.get("/get_user_data")
async def get_user(user_id: int) -> dict[str, list[str] | int | None]:
    try:
        user_id = int(user_id)
    except ValueError:
        http_handler.handle_http_err(status=400, msg="User ID is not an integer")

    user_data = db.get_user_data(user_id)

    if user_data:
        return user_data
    
    else:
        http_handler.handle_http_err(status=404, msg="User data not found")


@read_router.get("/get_all_users")
async def select_all():
    return db.select_all()
