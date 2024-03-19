#!/usr/bin/env python3

import logging
from make_env import get_env

class Logger:
    def __init__(self):
        env_variables = get_env()
        level = logging.DEBUG if env_variables["DEBUG"] else logging.WARNING
        logging_path = env_variables["LOG_PATH"]
        self.logger = logging.getLogger(__name__)
        formatter = logging.Formatter('%(levelname)s:%(asctime)s : %(name)s : %(message)s')
        file_handler = logging.FileHandler(f'{logging_path}/{__name__}.log')

        self.logger.setLevel(level)

        file_handler.setFormatter(formatter)


        if (self.logger.hasHandlers()):
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
