#!/usr/bin/env python3
from app.utils.env import get_var

import logging


class Logger:
    def __init__(self, fileName=__name__):
        level = logging.DEBUG if get_var("DEBUG") else logging.WARNING
        self.logger = logging.getLogger(__name__)
        self.fileName = fileName
        formatter = logging.Formatter(
            f"%(levelname)s:%(asctime)s : {self.fileName} : %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
        file_handler = logging.FileHandler(f"logs/{fileName}.log")

        self.logger.setLevel(level)

        file_handler.setFormatter(formatter)

        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        self.logger.addHandler(file_handler)

    def log_debug(self, debug):
        self.logger.debug(debug)

    def log_info(self, info):
        self.logger.info(info)

    def log_warning(self, warn):
        self.logger.warning(warn)

    def log_err(self, err):
        self.logger.error(err)

    def log_critical(self, crit):
        self.logger.critical(crit)
