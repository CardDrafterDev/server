from app.utils.env import get_var
from app.models import dataModels as models
import datetime

from fastapi.exceptions import HTTPException

import hashlib


def handle_admin_data(data: dict, session: models.Session):
    if not _check_ttl(session.exp):
        session.active = False
        raise HTTPException(401, "Session timeout")
    
    if not session.active:
        raise HTTPException(401, "Session not active")


def make_session(username: str, ttl: int, permissions: str, pswd: str | None = None) -> models.Session:
    if permissions == "admin":
        if not _verify_password(pswd=pswd, salt=get_var("PSWD_SALT")):
            raise HTTPException(401, "Password or login do not match")

    new_session = models.Session(
        username=username, 
        ttl=ttl, 
        exp=_make_ttl(ttl), 
        permissions=permissions, 
        session_id=_make_session_id(),
        active=True)

    return new_session


def _make_ttl(ttl: int) -> datetime.datetime:
    tz = datetime.timezone(datetime.timedelta(hours=3))
    now = datetime.datetime.now(tz=tz)
    timechange = datetime.timedelta(minutes=ttl)
    return now + timechange


def _check_ttl(expiration: datetime.datetime) -> bool:
    tz = datetime.timezone(datetime.timedelta(hours=3))
    now = datetime.datetime.now(tz=tz)
    if now > expiration:
        return False
    return True


def _make_session_id() -> str:
    tz = datetime.timezone(datetime.timedelta(hours=3))
    now = datetime.datetime.now(tz=tz)
    return hashlib.sha1(str(now).encode()).hexdigest()


def _verify_password(pswd: str, salt: str, admin_hash: str) -> bool:
    return admin_hash == _hash_pswd(pswd, salt).hexdigest()


def _hash_pswd(pswd, salt) -> str:
    return hashlib.md5(f"{pswd}.{salt}".encode())
