''' A Outhousers Database Model '''
from config.database import Model


class Outhousers(Model):

    __connection__ = 'connection_1'

    __table__ = "outhousers"
