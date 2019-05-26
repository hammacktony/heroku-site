''' A CBR Database Model '''
from config.database import Model


class Cbr(Model):
    
    __connection__ = 'postgres'
    __table__ = "cbr"
