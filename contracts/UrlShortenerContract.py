""" Url Shortener Contract """
from abc import ABC, abstractmethod


class UrlShortenerContract(ABC):

    @abstractmethod
    def shorten(self):
        """ Shorten Urls """


