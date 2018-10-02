''' A IGN Database Model '''
from config.database import Model


class Ign(Model):

    __connection__ = 'connection_1'

    __table__ = "ign"
