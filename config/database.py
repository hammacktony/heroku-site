"""Database Settings."""

import logging

from masonite import env
from masonite.environment import LoadEnvironment
from orator import DatabaseManager, Model

"""Load Environment Variables
Loads in the environment variables when this page is imported.
"""

LoadEnvironment()

"""Database Settings
Set connection database settings here as a dictionary. Follow the
format below to create additional connection settings.

Each key is a connection, not a driver. You may have as many
connections as you need.

Supported Drivers: 'sqlite', 'mysql', 'postgres'
"""

DATABASES = {
    'default': env('DB_CONNECTION'),
    'sqlite': {
        'driver': 'sqlite',
        'database': env('SQLITE_DB_DATABASE'),
        'log_queries': env('SQLITE_DB_LOG'),
    },
    'mysql': {
        'driver': 'mysql',
        'host': env('MYSQL_DB_HOST'),
        'database': env('MYSQL_DB_DATABASE'),
        'port': env('MYSQL_DB_PORT'),
        'user': env('MYSQL_DB_USERNAME'),
        'password': env('MYSQL_DB_PASSWORD'),
        'log_queries': env('MYSQL_DB_LOG'),
    },
    'postgres': {
        'driver': 'postgres',
        'host': env('POSTGRES_DB_HOST'),
        'database': env('POSTGRES_DB_DATABASE'),
        'port': env('POSTGRES_DB_PORT'),
        'user': env('POSTGRES_DB_USERNAME'),
        'password': env('POSTGRES_DB_PASSWORD'),
        'log_queries': env('POSTGRES_DB_LOG'),
    },
}

DB = DatabaseManager(DATABASES)
Model.set_connection_resolver(DB)


logger = logging.getLogger('orator.connection.queries')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    'It took %(elapsed_time)sms to execute the query %(query)s'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.addHandler(handler)
