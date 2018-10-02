''' A Newsarama Database Model '''
from config.database import Model


class Newsarama(Model):

    __connection__ = 'connection_1'

    __table__ = "newsarama"
