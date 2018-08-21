''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'HomeController@show').name('Brother Eye'),
    Get().route('/volcanoes', 'VolcanoesController@show').name('Brother Eye'),
    Get().route('/comics', 'ComicsController@show').name('Brother Eye'),
]
