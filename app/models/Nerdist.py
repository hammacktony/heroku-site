''' A Nerdist Database Model '''
from config.database import Model


class Nerdist(Model):

    __connection__ = 'connection_1'

    __table__ = "nerdist"
