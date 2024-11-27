from litestar import Litestar
from src.controlers.house import HouseController
from typing import cast
from sqlite3 import Connection, connect

DB_NAME = "houses.db"


def get_db_connection(app: Litestar) -> Connection:
    """Returns the db Connection.
    If it doesn't exist, creates it and saves it in on the application state object
    """
    if not getattr(app.state, "connection", None):
        app.state.connection = connect(DB_NAME)
    cursor = app.state.connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS houses(
                id INTEGER PRIMARY KEY ASC,
                address TEXT, 
                url TEXT)""")
    return cast(Connection, app.state.connection)


async def close_db_connection(app: Litestar) -> None:
    """Closes the db connection stored in the application State object."""
    # if getattr(app.state, "connection", None):
    #     cast(Connection, app.state.connection).close()
    return None


app = Litestar(route_handlers=[HouseController], on_startup=[get_db_connection], on_shutdown=[close_db_connection])
