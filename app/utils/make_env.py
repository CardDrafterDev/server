# loading data from .env

import os
from dotenv import load_dotenv


def get_env() -> dict[str, any]:
    load_dotenv()

    return dict(os.environ)
