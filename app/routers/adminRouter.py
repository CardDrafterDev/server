import app.models.dataModels as models

from app.auth import methods

import app.errorHandling.errorHandler as httperr

from fastapi import APIRouter
from fastapi import Request, Response, status, HTTPException

import os


admin_router = APIRouter()


@admin_router.post("/admin/login")
async def admin_panel(user: models.User, response: Response, request: Request):
    admin_user = methods.get_admin_user()
    if user.username == admin_user["username"] and methods.pwd_context.verify(
        user.password, admin_user["password"]
    ):
        access_token = methods.create_access_token(
            data={"sub": user.username}, expires_in=int(os.environ["TOKEN_EXP"])
        )
        methods.set_cookie(
            response=response,
            jwt_token=access_token,
            expires_in=int(os.environ["TOKEN_EXP"]),
        )
        return status.HTTP_202_ACCEPTED

    else:
        err = HTTPException(status_code=401, detail="Invalid username or password")
        handled_err = httperr.handle_http_exception(exc=err)
        return handled_err
