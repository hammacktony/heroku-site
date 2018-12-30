import requests
import os
from config.urlshortener import URL_SHORTENER
headers = {'Authorization': 'Bearer {}'.format(
    "d92e77ac7ccfe75a9e5764c573f911430b5fcb01")}

long_url = "http://www.tonyhammack.com/blog/tech/post/installing-ubuntu-18-04-on-dell-xps-laptops"


def shorten(**payload):
    """ Bitly Url Shortener 
    
    args
        **payload {dict} - json payload for api

    returns
        response {dict} - json response of query
    """

    # Bitly Api Endpoint
    api = "https://api-ssl.bitly.com/v4/bitlinks"

    # Headers for Bitly authorization (uses OAuth Token) 
    headers = {'Authorization': 'Bearer {token}'.format(token="d92e77ac7ccfe75a9e5764c573f911430b5fcb01")}

    r = requests.post(url=api, headers=headers, json=payload)

    # Appened status code to response
    status_code = {'status_code': r.status_code}
    response = {**r.json(), **status_code}
    return response


print(shorten(long_url=long_url, title="heo"))
