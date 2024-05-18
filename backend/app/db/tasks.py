import os
from fastapi import FastAPI
from databases import Database
from app.core.config import DATABASE_URL
import logging

logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI) -> None:
    DB_URL = f"{DATABASE_URL}_test" if os.environ.get("TESTING") else DATABASE_URL
    database = Database(DB_URL, min_size=2, max_size=10)

    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warning("--- DB CONNECTION ERROR ---")
        logger.warning(e)
        logger.warning("--- DB CONNECTION ERROR ---")


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warning("--- DB DISCONNECT ERROR ---")
        logger.warning(e)
        logger.warning("--- DB DISCONNECT ERROR ---")

# import os
# from fastapi import FastAPI
# from databases import Database
# from app.core.config import DATABASE_URL
# import logging
#
# logger = logging.getLogger(__name__)
#
# async def connect_to_db(app: FastAPI) -> None:
#     DB_URL = f"{DATABASE_URL}_test" if os.environ.get("TESTING") else DATABASE_URL
#     database = Database(DB_URL, min_size=2, max_size=10)
#     try:
#         await database.connect()
#         app.state.db = database  # Use a public variable instead of a private one
#     except Exception as e:
#         logger.warning("--- DB CONNECTION ERROR ---")
#         logger.warning(e)
#         # Consider re-raising critical exceptions
#         # raise e
#
# async def close_db_connection(app: FastAPI) -> None:
#     try:
#         if hasattr(app.state, 'db'):  # Check if the db connection exists
#             await app.state.db.disconnect()
#     except Exception as e:
#         logger.warning("--- DB DISCONNECT ERROR ---")
#         logger.warning(e)
#         # Consider re-raising critical exceptions
#         # raise e
