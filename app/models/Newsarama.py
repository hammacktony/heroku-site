''' A Newsarama Database Model '''
from config.database import Model


class Newsarama(Model):

    __connection__ = 'postgres'

    __table__ = "newsarama"
