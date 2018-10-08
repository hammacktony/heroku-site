''' User Model '''
from config.database import Model


class User(Model):
    ''' User Model '''

    __connection__ = 'connection_2'
    __fillable__ = ['name', 'email', 'password', 'is_admin', 'image', 'bio',
                    'website', 'facebook', 'twitter', 'github', 'gitlab', ]

    __auth__ = 'email'
