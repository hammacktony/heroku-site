""" User Api Resource """
from masonite.request import Request
from api.resources import Resource
from api.serializers import JSONSerializer
from app.User import User
from app.models.PersonalBlog import PersonalBlog

class UserResource(Resource, JSONSerializer):

    model = User
    methods = ['index']
    without = ['id', 'password', 'remember_token', 'is_admin',
               'created_at', 'updated_at', 'twitter', 'facebook', 'gitlab']

    def index(self, request: Request):
        """ Show user information """

        user_name = request.input('user')
        return self.model.where('user_name', user_name).get()
