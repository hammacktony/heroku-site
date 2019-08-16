"""Web Routes."""

from masonite.routes import Get, Post
from api.routes import JWTRoutes

from app.resources import PersonalBlogResource, TechnicalBlogResource, UserResource

ROUTES = [
    Get("/", "IndexController@show").name("main"),
    PersonalBlogResource("/api/personal").routes(),
    TechnicalBlogResource("/api/tech").routes(),
    UserResource('/api/user').routes(),
    JWTRoutes('/api/token'),
]
