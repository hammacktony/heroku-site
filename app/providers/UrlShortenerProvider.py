''' A UrlShortener Service Provider '''
from app.drivers import UrlShortenerBitlyDriver, UrlShortenerTinyurlDriver
from app.managers import UrlShortenerManager
from config import urlshortener
from masonite.provider import ServiceProvider


class UrlShortenerProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UrlShortenerConfig', urlshortener)
        self.app.bind('UrlShortenerBitlyDriver', UrlShortenerBitlyDriver)
        self.app.bind('UrlShortenerTinyurlDriver', UrlShortenerTinyurlDriver)
        self.app.bind('UrlShortenerManager', UrlShortenerManager(self.app))

    def boot(self, UrlShortenerConfig, UrlShortenerManager):
        self.app.bind('UrlShortenerManager', UrlShortenerManager.driver(
            self.app.make('UrlShortenerConfig').URL_SHORTENER_DRIVER))
