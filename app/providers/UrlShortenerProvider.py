''' A UrlShortener Service Provider '''
from config import urlshortener
from app.drivers import UrlShortenerBitlyDriver
from app.managers import UrlShortenerManager
from masonite.provider import ServiceProvider


class UrlShortenerProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UrlShortenerConfig', urlshortener)
        self.app.bind('UrlShortenerBitlyDriver', UrlShortenerBitlyDriver)
        self.app.bind('UrlShortenerManager', UrlShortenerManager(self.app))

    def boot(self, UrlShortenerConfig, UrlShortenerManager):
        self.app.bind('UrlShortener', UrlShortenerManager.driver(self.app.make('UrlShortenerConfig').DRIVER))
