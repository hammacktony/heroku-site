''' A blog Database Model '''
from config.database import Model

class blog(Model):
    __table__ = "posts"
    pass
