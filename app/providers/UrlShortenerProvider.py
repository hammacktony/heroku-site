''' A UrlShortener Service Provider '''
from app.drivers import UrlShortenerBitlyDriver
from app.managers.UrlShortenerManager import UrlShortenerManager
from config import urlshortener
from masonite.provider import ServiceProvider


class UrlShortenerProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UrlShortenerConfig', urlshortener)
        self.app.bind('UrlShortenerBitlyDriver', UrlShortenerBitlyDriver)
        self.app.bind('UrlShortenerManager', UrlShortenerManager(self.app))

    def boot(self, manager: UrlShortenerManager):
        self.app.bind('UrlShortener', manager.driver(urlshortener.URL_SHORTENER_DRIVER))
