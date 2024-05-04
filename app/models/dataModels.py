from pydantic import BaseModel
import datetime

class User(BaseModel):
    user_id: int
    collection: list[str] | None = None
    inventory: list[str] | None = None



class Session(BaseModel):
    ttl: int # ttl in seconds
    exp: datetime.datetime # session expiration datetime
    session_id: str
    username: str
    permissions: str
    active: bool



class AdminData(BaseModel):
    request_type: str