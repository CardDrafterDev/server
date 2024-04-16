from utils.make_env import get_env
from errorHandling.errorHandler import handle_db_err
from . import models

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

env = get_env()

DATABASE_URI = f"postgresql+psycopg2://{env["DB_USER"]}:{env["DB_PASSWORD"]}@{env["DB_HOST"]}:{env["DB_PORT"]}/{env["DB_NAME"]}"



def _db_create_session():
    engine = create_engine(DATABASE_URI)
    models.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()



s = _db_create_session()


def get_user_inventory(user_id: int) -> list[str]:
    try:
        inventory = s.query(models.User).filter_by(user_id=user_id).first()
        return inventory.inventory
    
    except Exception as e:
        handle_db_err(__name__, f"Could not get user inventory at table {env["TABLE_NAME"]}: {e}")





def get_user_collection(user_id: int) -> list[str]:
    try:
        collection = s.query(models.User).filter_by(user_id=user_id).first()
        return collection.collection
    
    except Exception as e:
        handle_db_err(__name__, f"Could not get user collection at table {env["TABLE_NAME"]}: {e}")
    

def update_user_inventory(user_id: int, inventory: list[str]) -> None:
    try:
        data = {
            "user_id": user_id,
            "inventory": inventory
            }
        query_text = text(f"""UPDATE {env["TABLE_NAME"]} SET inventory=ARRAY{inventory} WHERE user_id={user_id}""")
        s.execute(query_text, data)
        s.commit()
    except Exception as e:
        handle_db_err(__name__, f"Could not update inventory at table {env["TABLE_NAME"]}: {e}")
        raise e
    

    s.close()
def update_user_collection(user_id: int, collection: list[str]) -> None:
    try:
        data = {
            "user_id": user_id,
            "collection": collection
            }
        query_text = text(f"""UPDATE {env["TABLE_NAME"]} SET collection=ARRAY{collection} WHERE user_id={user_id}""")
        s.execute(query_text, data)
        s.commit()
    except Exception as e:
        handle_db_err(__name__, f"Could not update collection at table {env["TABLE_NAME"]}: {e}")
        raise e


def create_user(user_id: int) -> None:
    try:
        query_text = text(f"""INSERT INTO {env["TABLE_NAME"]} VALUES({user_id}, ARRAY[]::text[], ARRAY[]::text[])""")
        s.execute(query_text)
        s.commit()
    except Exception as e:
        handle_db_err(__name__, f"Could not create user at table {env["TABLE_NAME"]}: {e}")
        raise e
        

s.close()