from fastapi import HTTPException
from app.utils.logger import Logger


def handle_http_err(file_name: str , status: int, msg: str | None = None):
    logger = Logger(file_name)
    logger.log_err(
        err=HTTPException(
            status_code=status, 
            detail=msg)         
            )   
    
    raise HTTPException(status_code=status, detail=msg)



def handle_db_err(file_name: str, msg: str | None = None):
    logger = Logger(file_name)

    logger.log_err(
        err=msg
    )

    raise ConnectionError("Could not connect to db")
