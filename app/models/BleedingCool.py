''' A BleedingCool Database Model '''
from config.database import Model


class BleedingCool(Model):

    __connection__ = 'connection_1'
    __table__ = "bleedingcool"
