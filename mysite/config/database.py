import logging
"""Database Settings."""

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
    'default': {
        'driver': env('CONNECTION1_DB_DRIVER'),
        'host': env('CONNECTION1_DB_HOST'),
        'database': env('CONNECTION1_DB_DATABASE'),
        'user': env('CONNECTION1_DB_USERNAME'),
        'password': env('CONNECTION1_DB_PASSWORD'),
        'prefix': ''
    },
    'connection_2': {
        'driver': env('CONNECTION2_DB_DRIVER'),
        'host': env('CONNECTION2_DB_HOST'),
        'database': env('CONNECTION2_DB_DATABASE'),
        'user': env('CONNECTION2_DB_USERNAME'),
        'password': env('CONNECTION2_DB_PASSWORD'),
        'prefix': ''
    },
    'test': {
        'driver': env('test_DB_DRIVER'),
        'host': env('test_DB_HOST'),
        'database': env('test_DB_DATABASE'),
        'user': env('test_DB_USERNAME'),
        'password': env('test_DB_PASSWORD'),
        'prefix': ''
    }
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
