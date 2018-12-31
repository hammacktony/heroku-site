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
        "token": os.getenv("BITLY_API_TOKEN", None)
    }
}