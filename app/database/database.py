from app.utils.env import get_var
import app.errorHandling.errorHandler as error


from . import models

from sqlalchemy import text
from sqlalchemy import select

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




# DATABASE_URI = f"postgresql+psycopg2://{env['DB_USER']}:{env['DB_PASSWORD']}@{env['DB_HOST']}:{env['DB_PORT']}/{env['DB_NAME']}"
DATABASE_URI=get_var("DB_URI")
TABLE_NAME=get_var("TABLE_NAME")
print(TABLE_NAME)



def _db_create_session():
    engine = create_engine(DATABASE_URI)
    models.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()



db_handler = error.DBErrorHandler(__name__)


def get_user_data(user_id: int) -> models.User:
    with _db_create_session() as s:
    
        try:
            data = s.query(models.User).filter_by(user_id=user_id).first()
            if data:
                data_dict = {
                    "user_id": data.user_id,
                    "collection": data.collection,
                    "inventory": data.inventory
                }
                return data_dict
            
            
            return None
    
        except Exception as e:
            db_handler.handle_misc(msg=f"Could not get user data at table {TABLE_NAME}: {e}", e=e)


def select_all() -> list[models.User]:
    with _db_create_session() as s:
        try:
            statement = select(models.User).order_by(models.User.user_id)
            data = s.scalars(statement).all()
            return data
        except Exception as e:
            db_handler.handle_misc(msg=f"Could not SELECT * at table {TABLE_NAME}: {e}", e=e)
            raise e


def update_user_inventory(user_id: int, inventory: list[str]) -> None:
    with _db_create_session() as s:
        try:
            data = {
                "user_id": user_id,
                "inventory": inventory
                }
            query_text = text(f"""UPDATE {TABLE_NAME} SET inventory=ARRAY{inventory} WHERE user_id={user_id}""")
            s.execute(query_text, data)
            s.commit()
        except Exception as e:
            db_handler.handle_misc(msg=f"Could not update inventory at table {TABLE_NAME}: {e}", e=e)
            raise e


def update_user_collection(user_id: int, collection: list[str]) -> None:
    with _db_create_session() as s:
        try:
            data = {
                "user_id": user_id,
                "collection": collection
                }
            query_text = text(f"""UPDATE {TABLE_NAME} SET collection=ARRAY{collection} WHERE user_id={user_id}""")
            s.execute(query_text, data)
            s.commit()
        except Exception as e:
            db_handler.handle_misc(msg=f"Could not update collection at table {TABLE_NAME}: {e}", e=e)
            raise e


def create_user(user_id: int) -> None:
    with _db_create_session() as s:
        try:
            query_text = text(f"""INSERT INTO {TABLE_NAME}(user_id, collection, inventory) VALUES({user_id}, null, null)""")
            s.execute(query_text)
            s.commit()
        except Exception as e:
            if get_user_data(user_id):
                db_handler.handle_already_exists(f"User already exists at {TABLE_NAME}")
