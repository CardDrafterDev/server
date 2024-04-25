from app.middleware.cors import middleware
from app.utils.make_env import get_env
import app.routers.initRouter as Router


from fastapi import FastAPI, status

from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import RedirectResponse

from celery.app import Celery




server = FastAPI()

server.include_router(Router.Router)

DEFAULT_URL = "/docs"


@server.get("/", include_in_schema=False)
async def reroute_to_default():
    return RedirectResponse(url=DEFAULT_URL, status_code=status.HTTP_303_SEE_OTHER)




# env = get_env()
# redis_url = env["REDIS_URL"]


# celery_app = Celery(__name__, broker=redis_url, backend=redis_url)

# app.add_middleware(
#     CORSMiddleware,
#     *middleware
# )