import app.routers.initRouter as Router
from app.middleware.cors import add_cors


from fastapi import FastAPI, status

from starlette.responses import RedirectResponse

import ssl


server = FastAPI()

server.include_router(Router.Router)

add_cors(server)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")


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
