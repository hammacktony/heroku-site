""" Tech Blog Api Resource """
from api.resources import Resource
from api.serializers import JSONSerializer
from app.models import TechnicalBlog


class TechnicalBlogResource(Resource):

    model = TechnicalBlog
