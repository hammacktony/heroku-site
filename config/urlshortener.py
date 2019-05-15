''' Url Shortener Settings '''
from masonite import env

'''
|--------------------------------------------------------------------------
| Url Shortener
|-------------  -------------------------------------------------------------
|
| This is where you store the api keys. 
|
'''

URL_SHORTENER_DRIVER = env('URL_SHORTENER', 'bitly')

URL_SHORTENER = {
    "bitly": {
        "token": env("BITLY_API_TOKEN", None)
    },
    "tinyurl": "tinyurl",
}