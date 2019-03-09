""" Manger for Url Shorteners """
from masonite.managers import Manager

class UrlShortenerManager(Manager):
    
    config = 'UrlShortenerConfig'
    driver_prefix = 'UrlShortener'