import psycopg2 as psc2


from utils.make_env import get_env
from utils.logger import handle_db_err



def get_user_inventory(user_id: int) -> list[str]:
    env_vars = get_env()

    try:
        conn = psc2.connect(dbname=env_vars["DB_NAME_INV"], user=env_vars["USER"], password=env_vars["PASSWORD"], host=env_vars["HOST"])
        
    except:
        handle_db_err(__name__, f"Could not connect to the database {env_vars["DB_NAME_INV"]}")

    with conn.cursor as curs:
        curs.execute(f"SELECT inventory FROM Inventories WHERE user_id={user_id}")


def get_user_collection(user_id: int) -> list[str]:
    env_vars = get_env()

    try:
        conn = psc2.connect(dbname=env_vars["DB_NAME_COLL"], user=env_vars["USER"], password=env_vars["PASSWORD"], host=env_vars["HOST"])
        
    except:
        handle_db_err(__name__, f"Could not connect to the database {env_vars["DB_NAME_COLL"]}")


    with conn.cursor as curs:
        curs.execute(f"SELECT collection FROM Collection WHERE user_id={user_id}")
        


def put_user_collection(user_id: int, new_collection: list[str]) -> None:
    env_vars = get_env()

    try:
        conn = psc2.connect(dbname=env_vars["DB_NAME_COLL"], user=env_vars["USER"], password=env_vars["PASSWORD"], host=env_vars["HOST"])
        
    except:
        handle_db_err(__name__, f"Could not connect to the database {env_vars["DB_NAME_COLL"]}")


    with conn.cursor as curs:
        curs.execute()



def put_user_inventory(user_id: int, new_inventory: list[str]) -> None:
    env_vars = get_env()

    try:
        conn = psc2.connect(dbname=env_vars["DB_NAME_INV"], user=env_vars["USER"], password=env_vars["PASSWORD"], host=env_vars["HOST"])
        
    except:
        handle_db_err(__name__, f"Could not connect to the database {env_vars["DB_NAME_INV"]}")


    with conn.cursor as curs:
        curs.execute()