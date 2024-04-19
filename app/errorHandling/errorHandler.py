from fastapi import HTTPException
from app.utils.logger import Logger

    

class ErrorHandler:
    def __init__(self, file_name: str):
        self.file_name = file_name

    
class HttpErrorHandler(ErrorHandler):
    def handle_http_err(self, status: int, msg: str):
        logger = Logger(self.file_name)
        logger.log_err(
        err=HTTPException(
            status_code=status, 
            detail=msg)         
            )   
    
        raise HTTPException(status_code=status, detail=msg)


class DBErrorHandler(ErrorHandler):
    def handle_already_exists(self, msg: str):
        logger = Logger(self.file_name)

        logger.log_err(
            err=msg
        )

        raise HTTPException(409, detail=msg)
    

    def handle_misc(self, msg: str, e: Exception):
        logger = Logger(self.file_name)

        logger.log_err(
            err=msg
        )

        raise e
