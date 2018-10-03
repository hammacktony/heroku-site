''' A Nerdist Database Model '''
from config.database import Model


class Nerdist(Model):

    __connection__ = 'default'

    __table__ = "nerdist"
