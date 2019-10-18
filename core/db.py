""" Mongo DB Connection """
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from core.config import MONGO_DB, MONGO_HOST, MONGO_PORT, MONGO_PWD, MONGO_USER


def get_db() -> AsyncIOMotorDatabase:
    """ Make database connection """

    if not all([MONGO_HOST, MONGO_DB, MONGO_USER, MONGO_PWD]):
        # Just connect to the local machine database
        connection = AsyncIOMotorClient()
        db = connection.test_db
        return db

    # Connect to remote host and authenticate user
    connection = AsyncIOMotorClient(
        MONGO_HOST, MONGO_PORT, username=MONGO_USER, password=MONGO_PWD, authSource=MONGO_DB
    )
    db = connection[MONGO_DB]
    return db


db = get_db()
__all__ = ["db"]
