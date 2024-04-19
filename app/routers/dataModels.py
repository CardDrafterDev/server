from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    collection: list[str] | None = None
    inventory: list[str] | None = None