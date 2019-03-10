''' User Model '''
from config.database import Model


class User(Model):
    ''' User Model '''

    __connection__ = 'default'
    __fillable__ = ['name', 'email', 'password', 'is_admin', 'image', 'bio',
                    'website', 'facebook', 'linkedin', 'twitter', 'github', 'gitlab', ]

    __auth__ = 'email'
