from fastapi import HTTPException
from app.utils.logger import Logger


Logger = Logger()

def handle_http_err(status: int, msg = None):
    Logger.log_err(
        err=HTTPException(
            status_code=status, 
            detail=msg)
            )
    
    raise HTTPException(status_code=status, detail=msg)


