""" Personal Blog Api Resource """
from masonite.request import Request

from api.resources import Resource
from api.serializers import JSONSerializer
from app.models import PersonalBlog
from helpers.PostsHelpers import convert_slug_to_category


class PersonalBlogResource(Resource, JSONSerializer):

    model = PersonalBlog
    list_middleware = ['csrf']

    def index(self, request: Request):
        """ Return all posts """

        query = {
            'is_live': 1,
        }

        # Grab posts by category
        if request.input('category', None) is not None:
            query['category'] = convert_slug_to_category(
                request.input('category')
            )

        # Set limit of posts, defaults to None (Grabs all posts)
        limit = request.input('limit', None)

        return self.model.order_by(
            'updated_at', 'desc').where(query).take(limit).get()

    def show(self, request: Request):
        """ Return a post by slug """

        query = {
            'slug': request.param('id'),
            'is_live': 1,
        }

        return self.model.where(query).get()
