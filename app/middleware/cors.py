from fastapi.middleware.cors import CORSMiddleware
from app.utils.env import get_var


_origins = [
    f"https://{get_var('SERVER_HOST')}:{get_var('SERVER_PORT')}",
    f"http://{get_var('SERVER_HOST')}:{get_var('SERVER_PORT')}",
]


def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
