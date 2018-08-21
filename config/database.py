''' Database Settings '''

import os

from dotenv import find_dotenv, load_dotenv
from orator import DatabaseManager, Model

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

# DATABASES = {
#     'postgres': {
#         'driver': os.environ.get('DB_DRIVER'),
#         'host': os.environ.get('DB_HOST'),
#         'database': os.environ.get('DB_DATABASE'),
#         'user': os.environ.get('DB_USERNAME'),
#         'password': os.environ.get('DB_PASSWORD'),
#         'prefix': ''
#     }
# }

config = {
    'postgres': {
        'driver': 'postgres',
        'host': 'ec2-54-235-244-185.compute-1.amazonaws.com',
        'database': 'dfqefn9gk5dgnj',
        'user': 'pmnkiouizlkvpb',
        'password': 'e42ed49071fb7526e39693d62def04878ae1ae68058a1b3c6526eca0be120c64',
        'prefix': ''
    }
}

DB = DatabaseManager(config)
Model.set_connection_resolver(DB)
