from app.middleware.cors import middleware
from app.utils.make_env import get_env
import app.routers.initRouter as Router


from fastapi import FastAPI, status, Request

from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import RedirectResponse

from celery.app import Celery

import ssl




server = FastAPI()

server.include_router(Router.Router)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")


DEFAULT_URL = "/docs"


@server.get("/", include_in_schema=False)
async def reroute_to_default(request: Request):
    return RedirectResponse(url=DEFAULT_URL, status_code=status.HTTP_303_SEE_OTHER)



# env = get_env()
# redis_url = env["REDIS_URL"]


# celery_app = Celery(__name__, broker=redis_url, backend=redis_url)

# app.add_middleware(
#     CORSMiddleware,
#     *middleware
# )