from orator import DatabaseManager

config = {
    'mysql': {
        'driver': 'postgres',
        'host': 'ec2-54-235-244-185.compute-1.amazonaws.com',
        'database': 'dfqefn9gk5dgnj',
        'user': 'pmnkiouizlkvpb',
        'password': 'e42ed49071fb7526e39693d62def04878ae1ae68058a1b3c6526eca0be120c64',
        'prefix': ''
    }
}

db = DatabaseManager(config)