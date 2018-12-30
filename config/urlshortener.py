''' Url Shortener Settings '''
import os

'''
|--------------------------------------------------------------------------
| Url Shortener
|-------------  -------------------------------------------------------------
|
| This is where you store the api keys 
| framework needs to place the application's name in a notification or
| any other location as required by the application or its packages.
|
'''

DRIVER = os.getenv('URL_SHORTENER', 'bitly')

URL_SHORTENER = {
    "bitly": {
        "api_user": os.getenv("BITLY_API_USER", None),
        "api_key": os.getenv("BITLY_API_PASSWORD", None),
        "token": os.getenv("BITLY_API_TOKEN", None)
    }
}