""" Setup DB for Discord Bot"""
import json
import logging

from config.database import DATABASES
from orator import DatabaseManager, Schema

CONNECTION = 'test'

DB = DatabaseManager(DATABASES)
schema = Schema(DB)


# Initiate Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def create(table: str):
    """ Initialize Database """
    logger.info(f"Creating table {table}")
    with schema.connection(CONNECTION).create(table) as table:
        table.increments('id')
        table.string('slug')
        table.string('title')
        table.string('shortLink')

        table.string('image').nullable()
        table.string('category').nullable()

        table.integer('author_id').unsigned()
        # table.foreign('author_id').references('id').on('users')

        table.string('body', 10485760)
        table.timestamps()

        table.integer('is_live').nullable()
    logger.info(f"Table {table} created")


def delete(table: str):
    """ Cleanse Database """
    logger.info(f"Dropping table {table}")
    schema.connection(CONNECTION).drop(table)
    logger.info(f"Table {table} dropped")


if __name__ == "__main__":
    tables = ['blog', 'tech']

    # Create Database
    for table in tables:
        create(table)
