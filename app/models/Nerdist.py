''' A Nerdist Database Model '''
from config.database import Model


class Nerdist(Model):

    __connection__ = 'postgres'

    __table__ = "nerdist"
