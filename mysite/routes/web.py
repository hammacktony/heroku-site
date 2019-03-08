"""Web Routes."""
from app.resources import PersonalBlogResource
from app.resources import TechnicalBlogResource
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),

    # Api
    PersonalBlogResource('/api/blog/personal').routes(),
    TechnicalBlogResource('/api/blog/technical').routes(),
]
