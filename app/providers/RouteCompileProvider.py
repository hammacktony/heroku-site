''' A Route Compile Service Provider '''
from masonite.provider import ServiceProvider
from masonite.routes import Route

class RouteCompileProvider(ServiceProvider):
    ''' Adds Middleware To The Service Container '''

    wsgi = False


    def boot(self, route: Route):
        ''' Design custom route parameters '''
        route.compile('slug', r'[a-zA-Z]')
        route.compile('author', r'[a-zA-Z]')
        route.compile('category', r'[a-zA-Z]')
        route.compile('blog', r'[a-zA-Z]')