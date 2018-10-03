''' A Outhousers Database Model '''
from config.database import Model


class Outhousers(Model):

    __connection__ = 'default'

    __table__ = "outhousers"
