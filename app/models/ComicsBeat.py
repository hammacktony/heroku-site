''' A ComicsBeat Database Model '''
from config.database import Model


class ComicsBeat(Model):

    __connection__ = 'connection_1'

    __table__ = "comicsbeat"
