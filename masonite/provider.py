""" Module for the Service Provider """

from masonite.helpers import random_string


class ServiceProvider:
    """Service provider class. Used as mediator for loading objects or entire features into the container.
    """

    wsgi = True

    def __init__(self):
        """Service provider constructor
        """

        self.app = None

    def boot(self):
        """Used to boot things into the container. Typically ran after the register method has been ran.
        """

        pass

    def register(self):
        """Used to register objects into the container.
        """

        pass

    def load_app(self, app):
        """Load the container into the service provider.

        Arguments:
            app {masonite.app.App} -- Container object.

        Returns:
            self
        """

        self.app = app
        return self

    def routes(self, routes):
        web_routes = self.app.make('WebRoutes')
        web_routes += routes

    def http_middleware(self, middleware):
        http_middleware = self.app.make('HttpMiddleware')
        http_middleware += middleware

    def route_middleware(self, middleware):
        route_middleware = self.app.make('RouteMiddleware')
        route_middleware.update(middleware)

    def migrations(self, *directories):

        for directory in directories:
            self.app.bind(
                '{}_MigrationDirectory'.format(random_string(4)),
                directory
            )

    def commands(self, *commands):

        for command in commands:

            self.app.bind(
                '{}Command'.format(random_string(4)),
                command
            )

    def assets(self, assets):
        self.app.make('Storage').STATICFILES.update(assets)
