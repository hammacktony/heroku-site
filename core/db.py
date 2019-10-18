""" Mongo DB Connection """
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from core.config import MONGO


def get_db() -> AsyncIOMotorDatabase:
    """ Make database connection """

    if not all([MONGO.HOST.value, MONGO.DB.value, MONGO.USER.value, MONGO.PWD.value]):
        # Just connect to the local machine database
        connection = AsyncIOMotorClient()
        db = connection.test_db
        return db

    # Connect to remote host and authenticate user
    connection = AsyncIOMotorClient(
        MONGO.HOST.value,
        MONGO.PORT.value,
        username=MONGO.USER.value,
        password=MONGO.PWD.value,
        authSource=MONGO.DB.value,
    )
    db = connection[MONGO.DB.value]
    return db


db = get_db()
__all__ = ["db"]
