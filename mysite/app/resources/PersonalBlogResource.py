""" Personal Blog Api Resource """
from masonite.request import Request
from api.resources import Resource
from api.serializers import JSONSerializer
from app.models import PersonalBlog
from app.validators import ScopesValidator, PostValidator
from helpers.DashboardHelper import remove_whitespaces, slugify
from helpers.PostsHelpers import convert_slug_to_category


class PersonalBlogResource(Resource, JSONSerializer):

    model = PersonalBlog

    # Url of blog
    url = "http://www.tonyhammack.com/blog/personal/post/{}"

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

        request.status(200)
        return self.model.order_by(
            'updated_at', 'desc').where(query).take(limit).get()

    def show(self, request: Request):
        """ Return a post by slug """

        query = {
            'slug': request.param('id'),
            'is_live': 1,
        }

        response = self.model.where(query).get().serialize()

        if not response:
            request.status(410)  # TODO - Change to 404 in the future
            return {'status': 'post not found'}

        request.status(200)
        return response

    def create(self, UrlShortener, request: Request):  # , upload: Upload):
        """ Create new post """

        # TODO - Add Permissions with JWT
        # Make sure we have permission to be here
        scopes_validation = ScopesValidator(request)
        result = scopes_validation.validate('create')
        if not result:
            request.status(401)
            return {'error': 'cannot update post'}

        # Validate Entry
        validate = PostValidator(request)
        validate.register_form()

        # When we fail, alert us!
        if not validate.check():
            request.status(406)
            return {'error': validate.errors()}

        # TODO - Import image
        # Save image
        # try:
        #     ''' Deprecate storage location. Store images based on blog '''
        #     image = upload.driver('s3').store_prepend(
        #         request.input('file_upload'), 'blog/img/')

        #     # image = Upload.driver('s3').store_prepend(
        #     #     Request.input('file_upload'), 'tech/img/')
        # except AttributeError:
        #     # If user did not pick image, set image to none.
        #     image = None

        title = remove_whitespaces(request.input('title'))
        slug = slugify(title)
        body = remove_whitespaces(request.input('body'))
        category = remove_whitespaces(request.input('category', ''))

        # Check if post already exists, if so let us know
        if self.model.where("slug", slug).exists():
            request.status(403)
            return {'status': 'post already exists'}

        # Create shortened link for sharing
        short_link = UrlShortener.shorten(long_url=self.url.format(slug))

        post = {
            'title': title,
            'slug': slug,
            'body': body,
            'category': category,
            'image': None,    # TODO - Change in the future
            'author_id': 1,   # TODO - Change in the future
            'shortened_link': short_link.get('link', None),
            'is_live': 1,
        }

        # Create blog
        self.model.insert(post)

        request.status(201)
        return {'response': 'post created'}

    def update(self, UrlShortener, request: Request):
        " Update Post "

        # TODO - Add Permissions with JWT
        # Make sure we have permission to be here
        scopes_validation = ScopesValidator(request)
        result = scopes_validation.validate('update')
        if not result:
            request.status(401)
            return {'error': 'cannot update post'}

        # # Get post via slug
        post = self.model.where(
            'slug', request.param('id')).get().serialize()
        # dd(post)
        if not post:
            request.status(410)  # TODO - Change to 404 in the future
            return {'status': 'post not found'}

        # Updates Post
        update = dict()
        update['title'] = remove_whitespaces(
            request.input('title', post[0]['title']))
        update['slug'] = slugify(update['title'])
        update['body'] = remove_whitespaces(
            request.input('body', post[0]['body']))
        update['category'] = remove_whitespaces(
            request.input('category', post[0]['category']))

        # # Create shortened link for sharing
        shortened_url = UrlShortener.shorten(
            long_url=self.url.format(update['slug']))
        update['shortened_link'] = shortened_url.get("link", None)

        # Update post by id
        self.model.where('id', post[0]['id']).update(update)

        request.status(202)
        return {'status': 'updated'}

    def delete(self, request: Request):
        """ Deletes a Post """

        # TODO - Add Permissions with JWT
        # Make sure we have permission to be here
        scopes_validation = ScopesValidator(request)
        result = scopes_validation.validate('delete')
        if not result:
            request.status(401)
            return {'error': 'cannot delete post'}

        # Get slug from url
        slug = request.param('id')

        # Delete Post
        response = self.model.where('slug', slug).delete()

        if not response:
            request.status(410)  # TODO - Change to 404 in the future
            return {'status': 'post not found'}

        request.status(202)
        return {'status': 'deleted'}
