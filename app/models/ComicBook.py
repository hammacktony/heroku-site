''' A Comicbook Database Model '''
from config.database import Model


class ComicBook(Model):

    __connection__ = 'postgres'

    __table__ = "comicbook"
