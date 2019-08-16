from api.resources import Resource
from api.authentication import JWTAuthentication
from api.serializers import JSONSerializer
from app.models import Personal, Tech, User
from masonite.request import Request
from slugify import slugify


class PersonalBlogResource(Resource, JSONSerializer):
    model = Personal
    methods = ["index", "show"]
    without = ["is_live"]

    def index(self, request: Request):
        """ Return all posts """
        query = {"is_live": 1}

        if request.has("category"):
            query["category"] = request.input("category")

        if request.has("limit"):
            limit = int(request.input("limit"))
            return self.model.where(query).order_by("created_at", "desc").take(limit).get()

        return self.model.where(query).order_by("created_at", "desc").get()

    def show(self, request: Request):
        """ Return post by slug """
        query = {"slug": request.param("id").lower()}
        return self.model.where(query).get()

    def create(self, request: Request):
        """ Create new post """
        self.model.create(
            slug=slugify(request.input("title")),
            title=request.input("title"),
            image="",
            category=slugify(request.input("category").lower()),
            body=request.input("body"),
            is_live=1,
            author_id=1,
            shortehned_url="",
        )
        return ""

    def update(self, request: Request):
        """ Update post """
        collection = self.model.where("slug", request.param("id")).get()
        collection[0].title = request.input("title")
        collection[0].slug = slugify(collection[0].title)
        collection[0].body = request.input("body")
        collection[0].category = slugify(request.input("category"))

        # TODO - URL Shorten

        # Update post
        collection[0].save()
        return self.model.where("slug", request.param("id")).get()

    def delete(self, request: Request):
        """ Delete post """
        try:
            collection = self.model.where("slug", request.param("id")).get()
            collection[0].delete()
        except IndexError:
            pass
        return ""
