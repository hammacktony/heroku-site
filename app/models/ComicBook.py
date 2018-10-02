''' A Comicbook Database Model '''
from config.database import Model


class ComicBook(Model):

    __connection__ = 'connection_1'

    __table__ = "comicbook"
