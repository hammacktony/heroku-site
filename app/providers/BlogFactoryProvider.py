''' A MiddlewareProvider Service Provider '''
from masonite.provider import ServiceProvider
from app.models.blog import BlogFactory

class BlogFactoryProvider(ServiceProvider):
    ''' Adds Middleware To The Service Container '''

    wsgi = False

    def register(self):
        ''' Register Middleware Into The Service Container '''
        self.app.bind('BlogFactory', BlogFactory)

    def boot(self):
        pass
