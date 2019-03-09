""" Tech Blog Api Resource """
from masonite.request import Request
from api.resources import Resource
from api.serializers import JSONSerializer
from app.models import TechnicalBlog
from app.validators import PostValidator
from helpers.DashboardHelper import remove_whitespaces, slugify
from helpers.PostsHelpers import convert_slug_to_category


class TechnicalBlogResource(Resource, JSONSerializer):

    model = TechnicalBlog
    # list_middleware = ['csrf']

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

        # TODO - Grab posts by author
        # Grab posts by author
        # if request.input('author', None) is not None:
        #     query['category'] = convert_slug_to_category(
        #         request.input('category')

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

    def create(self, UrlShortener, request: Request):  # , upload: Upload): 
        """ Create new post """

        # Validate Entry
        validate = PostValidator(request)
        validate.register_form()

        # When we fail, alert us!
        if not validate.check():
            request.status(412)
            return {'error': validate.errors()}

        # TODO - Import image
        # Save image
        # try:
        #     ''' Deprecate storage location. Store images based on blog '''
        #     image = upload.driver('s3').store_prepend(
        #         request.input('file_upload'), 'blog/img/')

        #     # image = Upload.driver('s3').store_prepend(
        #     #     Request.input('file_upload'), '{}/img/'.format(self.blog_name))
        # except AttributeError:
        #     # If user did not pick image, set image to none.
        #     image = None

        slug = slugify(remove_whitespaces(request.input('title')))

        # Get full url of article
        url = f"http://www.tonyhammack.com/blog/tech/post/{slug}"

        # Create shortened link for sharing
        shortened_url = UrlShortener.shorten(long_url=url)
        try:
            link = shortened_url["link"]
        except KeyError:
            link = None
            
        # Create blog
        self.model.create(
            title=remove_whitespaces(request.input('title')),
            slug=slug,
            category=remove_whitespaces(request.input('category')),
            body=remove_whitespaces(request.input('body')),
            image=None,
            author_id=1, # TODO - Dynamically set author,
            shortened_url=link,
            is_live=1
        )

        request.status(201)
        return {'response': 'post created'}
