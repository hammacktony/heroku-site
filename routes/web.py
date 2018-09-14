''' Web Routes '''
from masonite.routes import Get, Post
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    # Index
    Get().route('/', 'HomeController@show'),
    # Contact
    Get().route('/contact', 'ContactController@show'),
    Post().route('/contact', 'ContactController@store'),
    # Projects
    Get().route('/projects', 'ProjectsController@show'),
    Get().route('/volcanoes', 'VolcanoesController@show'),
    # Comics
    Get().route('/comics', 'ComicsController@show'),
    # Dashboard
    DashboardRoutes(),
    Get().route('/dashboard/helloworld', 'HelloWorldController@show'),
    # Dashboard - Blog
    # Get().route('/dashboard/blog', 'BlogController@show'),
    # Post().route('/dashboard/blog/create', 'BlogController@store'),
    # Posts
    # Get().route('/posts', 'PostController@show'),
    # Get().route('/post/@id', 'PostController@single'),
    # Get().route('/post/@id/update', 'PostController@update'),
    # Post().route('/post/@id/update', 'PostController@store'),
    # Get().route('/post/@id/delete', 'PostController@delete')
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    # Get().route('/register', 'RegisterController@show'),
    # Post().route('/register', 'RegisterController@store'),
    
]
