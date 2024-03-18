from fastapi import FastAPI, HTTPException
from app.utils.logger import Logger

def log_err(err: HTTPException, msg: str | None):
    ...
