"""Bitly Url Shortener driver."""
import os

import requests

from app.contracts import UrlShortenerContract
from app.managers import UrlShortenerManager
from masonite.drivers.BaseDriver import BaseDriver


class UrlShortenerTinyurlDriver(UrlShortenerContract, BaseDriver):
    """Bitly Url Shortener driver."""

    # Source: https://dev.bitly.com/v4_documentation.html

    def __init__(self, UrlShortenerConfig):
        """ Url Shortener Driver Constructor """

    def shorten(self, long_url: str):
        """ Tiny Url Url Shortener 
        
        args
            long_url - url to be shortened

        returns
            response {dict} - json response of query
        """

        # Make sure the long url is present
        if not long_url:
            return None

        # TinyUrl Api Endpoint
        api = "http://tinyurl.com/api-create.php?url={url}".format(url=long_url)

        # Headers for Bitly authorization (uses OAuth Token) 
        r = requests.post(url=api)

        # Appened status code to response
        response = {'link': r.text, 'status_code': r.status_code}
        return response
