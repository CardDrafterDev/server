from pydantic import BaseModel

class Card(BaseModel):
    id: str
    name: str
    img: str | None = None
    description: str | None = None




class User(BaseModel):
    tg_id: str
    inventory: list[Card]
    collection: list[Card]