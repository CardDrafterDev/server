from fastapi import FastAPI, status

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from celery.app import Celery


from app.middleware.cors import middleware
from app.utils.make_env import get_env
import app.routers.initRouter as Router



server = FastAPI()

server.include_router(Router.Router)


@server.get("/")
async def docs():
    return RedirectResponse("/docs", status_code=status.HTTP_303_SEE_OTHER)


# env = get_env()
# redis_url = env["REDIS_URL"]


# celery_app = Celery(__name__, broker=redis_url, backend=redis_url)

# app.add_middleware(
#     CORSMiddleware,
#     *middleware
# )