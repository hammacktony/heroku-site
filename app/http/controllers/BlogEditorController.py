''' A Controller to create, update, and delete blog entries '''
from app.User import User
from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View
from app.models.blog import Blog

from lib.helpers.DashboardHelper import remove_whitespaces, slugify
from app.managers.UrlShortenerManager import UrlShortenerManager
from masonite.managers import UploadManager
from mistune import Markdown


class BlogEditorController(object):
    ''' Dashboard Blog Controller '''

    def __init__(self, request: Request):
        """ Set blog table at runtime """
        self.blog_name = Request.param('blog').lower()
        self.Blog = Blog().make(self.blog_name)

    def show_all(self, request: Request, view: View):
        """ Display all posts in blog editor """

        posts = self.Blog.order_by(
            'updated_at', 'desc').get()

        return view.render('dashboard/blog/home', {'author': User, 'Auth': Auth(request),
                                            'posts': posts, 'blog': self.blog_name})

    def show_create(self, request: Request, view: View):
        """ Display page to create post"""

        return view.render('dashboard/blog/post/create', {'Auth': Auth(request), 'blog': self.blog_name})

    def create(self, request: Request, upload: UploadManager, url: UrlShortenerManager, view: View):
        """ Create new post """

        # Save image
        try:
            ''' Deprecate storage location. Store images based on blog '''
            image = upload.driver('s3').store_prepend(
                request.input('file_upload'), 'blog/img/')

            # image = Upload.driver('s3').store_prepend(
            #     request.input('file_upload'), '{}/img/'.format(self.blog_name))
        except AttributeError:
            # If user did not pick image, set image to none.
            image = None

        # Create slug
        slug = slugify(remove_whitespaces(request.input('title')))

        # Get full url of article
        full_url = "http://www.tonyhammack.com/blog/{blog}/post/{slug}".format(
            blog=self.blog_name, slug=slug)

        # Create shortened link for sharing
        shortened_url = url.shorten(long_url=full_url)
        link = shortened_url.get("link", None)

        # Create blog
        self.Blog.create(
            title=remove_whitespaces(request.input('title')),
            slug=slug,
            category=remove_whitespaces(request.input('category')),
            body=remove_whitespaces(request.input('body')),
            image=image,
            author_id=request.user().id,
            shortened_url=link,
            is_live=1
        )

        return request.redirect('dashboard/blog/{}/home'.format(self.blog_name), {'Auth': Auth(request), 'blog': self.blog_name})

    def show_update(self, request: Request, view: View):
        """ Display Post Update page """

        # Get post via slug
        posts = self.Blog.where('slug', request.param('slug')).get()

        return view.render('dashboard/blog/post/update', {'post': posts[0], 'Auth': Auth(request), 'blog': self.blog_name})

    def update(self, request: Request, upload: UploadManager, url: UrlShortenerManager):
        """ Update Post Controller """

        # Get post via slug
        posts = self.Blog.where('slug', request.param('slug')).get()

        # Updates Post
        posts[0].title = remove_whitespaces(request.input('title'))
        posts[0].slug = slugify(posts[0].title)
        posts[0].body = remove_whitespaces(request.input('body'))
        posts[0].category = remove_whitespaces(request.input('category'))

        # Get full url of article
        full_url = "http://www.tonyhammack.com/blog/{blog}/post/{slug}".format(
            blog=self.blog_name, slug=posts[0].slug)

        # Create shortened link for sharing
        shortened_url = url.shorten(long_url=full_url)
        posts[0].link = shortened_url.get("link", None)

        # Update post
        posts[0].save()

        return request.redirect('dashboard/blog/{}/home'.format(self.blog_name), {'Auth': Auth(request)})

    def show_delete(self, request: Request, view: View):
        """ Display Post Delete page """

        # Get post via slug
        posts = self.Blog.where('slug', request.param('slug')).get()

        return view.render('dashboard/blog/post/delete', {'post': posts[0], 'Auth': Auth(request), 'blog': self.blog_name})

    def delete(self, request: Request):
        """ Delete Post Controller """

        # Get post via slug
        posts = self.Blog.where('slug', request.param('slug')).get()

        posts[0].delete()

        return request.redirect('dashboard/blog/{}/home'.format(self.blog_name), {'Auth': Auth(request), 'blog': self.blog_name})

    def preview(self, request: Request, markdown: Markdown, view: View):
        """ Display all posts in blog editor """

        # Get post via slug
        posts = self.Blog.where('slug', request.param('slug')).get()
        posts[0].body = markdown(posts[0].body)

        return view.render('dashboard/blog/post/preview', {'author': User, 'Auth': Auth(request),
                                                    'posts': posts[0]})

    def activate(self, request: Request):
        """ Activates post to be displayed """

        # Get post via slug
        posts = self.Blog.where('slug', request.param('slug')).get()
        posts[0].is_live = 1
        posts[0].save()

        return request.redirect('dashboard/blog/{}/home'.format(self.blog_name), {'Auth': Auth(request), 'blog': self.blog_name})

    def deactivate(self, request: Request):
        """ Removes post from active list """

        # Get post via slug
        posts = self.Blog.where('slug', request.param('slug')).get()
        posts[0].is_live = 0
        posts[0].save()

        return request.redirect('dashboard/blog/{}/home'.format(self.blog_name), {'Auth': Auth(request), 'blog': self.blog_name})
