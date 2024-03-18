import logging
from make_env import get_env

class Logger:
    def __init__(self):
        self.debug = get_env()["DEBUG"]
