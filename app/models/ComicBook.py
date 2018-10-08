''' A Comicbook Database Model '''
from config.database import Model


class ComicBook(Model):

    __connection__ = 'default'

    __table__ = "comicbook"
