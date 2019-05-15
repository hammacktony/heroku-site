"""Bitly Url Shortener driver."""
import os

import requests

from app.contracts import UrlShortenerContract
from app.managers import UrlShortenerManager
from masonite.drivers.BaseDriver import BaseDriver


class UrlShortenerBitlyDriver(UrlShortenerContract, BaseDriver):
    """Bitly Url Shortener driver."""

    # Source: https://dev.bitly.com/v4_documentation.html

    def __init__(self, UrlShortenerConfig):
        """ Url Shortener Driver Constructor
        Arguments:
            url_shortener {masonite.managers.UrlShortenerManager} -- The URL Shortener Manager object.
            UrlShortenerConfig {config.urlshortener} -- Url shortenr config  configuration.
        """
        self.config = UrlShortenerConfig.URL_SHORTENER


    def shorten(self, **payload):
        """ Bitly Url Shortener 
        
        args
            **payload {dict} - json payload for api

        returns
            response {dict} - json response of query
        """

        # Bitly Api Endpoint
        api = "https://api-ssl.bitly.com/v4/bitlinks"

        # Headers for Bitly authorization (uses OAuth Token) 
        headers = {'Authorization': 'Bearer {token}'.format(token=self.config["bitly"]["token"])}

        r = requests.post(url=api, headers=headers, json=payload)

        # Appened status code to response
        status_code = {'status_code': r.status_code}
        response = {**r.json(), **status_code}
        return response
