from fastapi.middleware.cors import CORSMiddleware
from app.utils.make_env import get_env


env_variables = get_env()

_origins = [
    f"https://{env_variables['SERVER_HOST']}:{env_variables['SERVER_PORT']}",
    f"http://{env_variables['SERVER_HOST']}:{env_variables['SERVER_PORT']}",

]


cors_regex = ...

middleware = [
    _origins,

]


def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )