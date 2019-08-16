''' Database Model for Personal Blog '''
from config.database import Model
from orator.orm import belongs_to
from orator.orm import scope
from app.models import User


class Personal(Model):
    __connection__ = 'mysql'
    # __connection__ = 'sqlite'

    __table__ = "personal"

    __fillable__ = ['title',
                    'author_id',
                    'body',
                    'category',
                    'slug',
                    'image',
                    'shortened_url',
                    'is_live']

    @belongs_to('author_id', 'id')
    def author(self):
        return User
