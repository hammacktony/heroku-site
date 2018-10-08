''' A Route Compile Service Provider '''
from masonite.provider import ServiceProvider

class RouteCompileProvider(ServiceProvider):
    ''' Adds Middleware To The Service Container '''

    wsgi = False


    def boot(self, Route):
        ''' Design custom route parameters '''
        Route.compile('slug', r'[a-zA-Z-]')
        Route.compile('author', r'[a-zA-Z]')
        Route.compile('category', r'[a-zA-Z]')