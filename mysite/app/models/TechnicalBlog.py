''' A Post Database Model '''
from orator.orm import belongs_to, scope

from app.User import User
from config.database import Model


class TechnicalBlog(Model):

    __connection__ = 'connection_2'

    __table__ = "tech"
    
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
