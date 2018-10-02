''' A CBR Database Model '''
from config.database import Model


class Cbr(Model):
    
    __connection__ = 'connection_1'
    __table__ = "cbr"
