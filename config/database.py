''' Database Settings '''

import os

from dotenv import find_dotenv, load_dotenv
from orator import DatabaseManager, Model, Schema

'''
|--------------------------------------------------------------------------
| Load Environment Variables
|--------------------------------------------------------------------------
|
| Loads in the environment variables when this page is imported.
|
'''

load_dotenv(find_dotenv())

'''
|--------------------------------------------------------------------------
| Database Settings
|--------------------------------------------------------------------------
|
| Set connection database settings here as a dictionary. Follow the
| format below to create additional connection settings.
|
| @see Orator migrations documentation for more info
|
'''

DATABASES = {
	'default': {
       'driver': os.environ.get('CONNECTION1_DB_DRIVER'),
       'host': os.environ.get('CONNECTION1_DB_HOST'),
       'database': os.environ.get('CONNECTION1_DB_DATABASE'),
       'user': os.environ.get('CONNECTION1_DB_USERNAME'),
       'password': os.environ.get('CONNECTION1_DB_PASSWORD'),
       'prefix': ''
   },
   'connection_2': {
       'driver': os.environ.get('CONNECTION2_DB_DRIVER'),
       'host': os.environ.get('CONNECTION2_DB_HOST'),
       'database': os.environ.get('CONNECTION2_DB_DATABASE'),
       'user': os.environ.get('CONNECTION2_DB_USERNAME'),
       'password': os.environ.get('CONNECTION2_DB_PASSWORD'),
       'prefix': ''
   },
}

DB = DatabaseManager(DATABASES)
SCHEMA= Schema(DB)
Model.set_connection_resolver(DB)
