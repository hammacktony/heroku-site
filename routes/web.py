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
    # Get().route('/comics', 'ComicsController@show'),
    
    # Blog
    RouteGroup([
        Get().route('/blog', 'PostsController@show_all'),
        Get().route('/blog/post/@slug', 'PostsController@show_one'),
        Get().route('/blog/category/@catgory', 'PostsController@show_category'),
        Get().route('/blog/author/@author', 'PostsController@show_author'),
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
        RouteGroup([
            Get().route('/main', 'BlogEditorController@show_all'),

                # Blog Editor
                RouteGroup([
                    Get().route('/create', 'BlogEditorController@show_create'),
                    Post().route('/create', 'BlogEditorController@create'),

                    Get().route('/@slug/update', 'BlogEditorController@show_update'),
                    Post().route('/@slug/update', 'BlogEditorController@update'),

                    Get().route('/@slug/delete', 'BlogEditorController@show_delete'),
                    Post().route('/@slug/delete', 'BlogEditorController@delete'),

                    Get().route('/@slug/activate', 'BlogEditorController@activate'),
                    Get().route('/@slug/deactivate', 'BlogEditorController@deactivate'),

                    Get().route('/preview/@slug', 'BlogEditorController@preview')
                ], prefix="/post")

            ], prefix="/blog")        

    ], prefix='/dashboard', middleware=('auth',))

]

# ROUTES = ROUTES + [
#     Get().route('/login', 'LoginController@show'),
#     Get().route('/logout', 'LoginController@logout'),
#     Post().route('/login', 'LoginController@store'),
#     Get().route('/register', 'RegisterController@show'),
#     Post().route('/register', 'RegisterController@store'),
    
# ]
