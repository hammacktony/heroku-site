"""Web Routes."""
from masonite.routes import Get, Post

from api.routes import JWTRoutes
from app.resources import (PersonalBlogResource, TechnicalBlogResource,
                           UserResource)

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),

    # Api
    PersonalBlogResource('/api/blog/personal').routes(),
    TechnicalBlogResource('/api/blog/technical').routes(),
    UserResource('/api/user').routes(),
    JWTRoutes('/api/token'),
]
