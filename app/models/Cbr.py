''' A CBR Database Model '''
from config.database import Model


class Cbr(Model):
    
    __connection__ = 'default'
    __table__ = "cbr"
