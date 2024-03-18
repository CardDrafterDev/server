from pydantic import BaseModel

class Card(BaseModel):
    id: str
    name: str
    description: str | None = None



class User(BaseModel):
    tg_id: str
    cards: list[str]
    