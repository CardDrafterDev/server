from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    collection = Column(ARRAY(String))
    inventory = Column(ARRAY(String))

    def __repr__(self):
        return f"<User(user_id='{self.user_id}', collection='{self.collection}', inventory='{self.inventory}')>"
    