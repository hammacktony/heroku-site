''' A BleedingCool Database Model '''
from config.database import Model


class BleedingCool(Model):

    __connection__ = 'postgres'
    __table__ = "bleedingcool"
