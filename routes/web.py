''' Web Routes '''
from masonite.routes import Get, Post
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    # Index
    Get().route('/', 'HomeController@show').name('Brother Eye'),
    # Contact
    Get().route('/contact', 'ContactController@show').name('Brother Eye'),
    Post().route('/contact', 'ContactController@store').name('Brother Eye'),
    # Projects
    Get().route('/projects', 'ProjectsController@show').name('Brother Eye'),
    Get().route('/projects/volcanoes', 'VolcanoesController@show').name('Brother Eye'),
    # Comics
    Get().route('/comics', 'ComicsController@show').name('Brother Eye'),
    # Dashboard
    DashboardRoutes(),
    Get().route('/dashboard/helloworld', 'HelloWorldController@show'),
    # Dashboard - Blog
    # Get().route('/dashboard/blog', 'BlogController@show').name('Brother Eye'),
    # Post().route('/dashboard/blog/create', 'BlogController@store'),
    # Posts
    # Get().route('/posts', 'PostController@show').name('Brother Eye'),
    # Get().route('/post/@id', 'PostController@single').name('Brother Eye'),
    # Get().route('/post/@id/update', 'PostController@update').name('Brother Eye'),
    # Post().route('/post/@id/update', 'PostController@store').name('Brother Eye'),
    # Get().route('/post/@id/delete', 'PostController@delete').name('Brother Eye')
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    # Get().route('/register', 'RegisterController@show'),
    # Post().route('/register', 'RegisterController@store'),
    
]
