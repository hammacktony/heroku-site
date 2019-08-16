from api.resources import Resource
from api.authentication import JWTAuthentication
from api.serializers import JSONSerializer
from app.models import User
from masonite.request import Request
from slugify import slugify


class UserResource(Resource, JSONSerializer):
    model = User
    methods = ["show"]
    without = ["id", "email", "password", "remember_token", "is_admin", "created_at", "updated_at", "user_name"]

    def show(self, request: Request):
        user = request.param("id").lower()
        return self.model.where("user_name", user).get()
