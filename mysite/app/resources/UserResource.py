""" User Api Resource """
from masonite.request import Request
from api.resources import Resource
from api.authentication import JWTAuthentication
from api.serializers import JSONSerializer
from app.User import User


class UserResource(Resource, JSONSerializer, JWTAuthentication):

    model = User
