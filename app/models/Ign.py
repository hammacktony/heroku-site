''' A IGN Database Model '''
from config.database import Model


class Ign(Model):

    __connection__ = 'postgres'

    __table__ = "ign"
