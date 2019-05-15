''' User Model '''
from config.database import Model


class User(Model):
    ''' User Model '''

    __connection__ = "default"
    __table__ = 'users'
    __fillable__ = ['name', 'email', 'password', 'is_admin', 'image', 'bio',
                    'website', 'facebook', 'linkedin', 'twitter', 'github', 'gitlab', 'devto']

    __auth__ = 'email'
