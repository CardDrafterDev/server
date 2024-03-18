from fastapi import FastAPI, HTTPException


def log_err(err: HTTPException, msg: str | None):
    ...


