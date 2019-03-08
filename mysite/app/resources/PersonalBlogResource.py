""" Personal Blog Api Resource """
from api.resources import Resource
from api.serializers import JSONSerializer
from app.models import PersonalBlog


class PersonalBlogResource(Resource):

    model = PersonalBlog
