''' A Post Database Model '''
from config.database import Model
from orator.orm import belongs_to
from orator.orm import scope
from app.User import User


class PersonalBlog(Model):
    __connection__ = 'default'

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
