''' Web Routes '''
from masonite.routes import Get, Post
from dashboard.routes import routes as DashboardRoutes
ROUTES = [
    Get().route('/', 'HomeController@show').name('Brother Eye'),

    Get().route('/projects', 'ProjectsController@show').name('Brother Eye'),
    Get().route('/projects/volcanoes', 'VolcanoesController@show').name('Brother Eye'),

    Get().route('/comics', 'ComicsController@show').name('Brother Eye'),

    Get().route('/blog', 'BlogController@show').name('Brother Eye'),
    Post().route('/blog/create', 'BlogController@store'),
    
    Get().route('/posts', 'PostController@show').name('Brother Eye'),
    Get().route('/post/@id', 'PostController@single').name('Brother Eye'),
    Get().route('/post/@id/update', 'PostController@update').name('Brother Eye'),
    Post().route('/post/@id/update', 'PostController@store').name('Brother Eye'),
    Get().route('/post/@id/delete', 'PostController@delete').name('Brother Eye')
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    DashboardRoutes(),
    Get().route('/dashboard/helloworld', 'HelloWorldController@show'),
]
