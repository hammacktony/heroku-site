''' Url Shortener Settings '''
import os

'''
|--------------------------------------------------------------------------
| Url Shortener
|-------------  -------------------------------------------------------------
|
| This is where you store the api keys. 
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