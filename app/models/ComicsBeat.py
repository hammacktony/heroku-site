''' A ComicsBeat Database Model '''
from config.database import Model


class ComicsBeat(Model):

    __connection__ = 'postgres'

    __table__ = "comicsbeat"
