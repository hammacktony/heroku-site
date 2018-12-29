''' Web Routes '''
from masonite.routes import Get, Post, RouteGroup
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

    # Blog
    RouteGroup([
        Get().route('/@blog', 'PostsController@show_all'),
        Get().route('/@blog/post/@slug', 'PostsController@show_one'),
        Get().route('/@blog/category/@category', 'PostsController@show_category'),
        Get().route('/@blog/author/@author', 'PostsController@show_author')
    ]),


    # Dashboard
    DashboardRoutes(),
    RouteGroup([

        # Dashboard - User
        RouteGroup([
            Get().route('/profile', 'ProfileController@show'),
            Post().route('/profile', 'ProfileController@store'),
        ], prefix="/user"),

        # Dashboard - Blog
            Get().route('/blog/@blog/home', 'BlogEditorController@show_all'),

            # Blog Editor
            Get().route('/blog/@blog/post/create', 'BlogEditorController@show_create'),
            Post().route('/blog/@blog/post/create', 'BlogEditorController@create'),

            Get().route('/blog/@blog/post/@slug/update', 'BlogEditorController@show_update'),
            Post().route('/blog/@blog/post/@slug/update', 'BlogEditorController@update'),

            Get().route('/blog/@blog/post/@slug/delete', 'BlogEditorController@show_delete'),
            Post().route('/blog/@blog/post/@slug/delete', 'BlogEditorController@delete'),

            Get().route('/blog/@blog/post/@slug/activate', 'BlogEditorController@activate'),
            Get().route('/blog/@blog/post/@slug/deactivate', 'BlogEditorController@deactivate'),

            Get().route('/blog/@blog/post/preview/@slug', 'BlogEditorController@preview')


    ], prefix='/dashboard', middleware=('auth',))

]

# ROUTES = ROUTES + [
#     Get().route('/login', 'LoginController@show'),
#     Get().route('/logout', 'LoginController@logout'),
#     Post().route('/login', 'LoginController@store'),
#     Get().route('/register', 'RegisterController@show'),
#     Post().route('/register', 'RegisterController@store'),

# ]
