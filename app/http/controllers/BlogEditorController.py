''' A Controller to create, update, and delete blog entries '''
from app.Post import Post
from app.User import User
from masonite.facades.Auth import Auth

from helpers.DashboardHelper import remove_whitespaces, slugify


class BlogEditorController(object):
    ''' Dashboard Blog Controller '''

    def __init__(self):
        pass

    def show_all(self, Request):
        """ Display all posts in blog editor """

        posts = Post.all()

        return view('dashboard/blog/main', {'author': User, 'Auth': Auth(Request),
                                       'posts': posts})

    def show_create(self, Request):
        """ Display page to create post"""

        return view('dashboard/blog/post/create', {'Auth': Auth(Request)})

    def create(self, Request, Upload):
        """ Create new post """

        # Save image
        try:
            image = Upload.driver('s3').store_prepend(Request.input('file_upload'), 'blog/img/')
        except AttributeError:
            # If user did not pick image, set image to none. (Load default)
            image = "nightlife1.jpg"

        Post.create(
            title=remove_whitespaces(Request.input('title')),
            slug=slugify(remove_whitespaces(Request.input('title'))),
            category=remove_whitespaces(Request.input('category')),
            body=remove_whitespaces(Request.input('body')),
            image=image,
            author_id=Request.user().id,
            is_live=1
        )

        return Request.redirect('dashboard/blog/main', {'Auth': Auth(Request)})

    def show_update(self, Request):
        """ Display Post Update page """

        # Get post via slug
        posts = Post.where('slug', Request.param('slug')).get()

        return view('dashboard/blog/post/update', {'post': posts[0], 'Auth': Auth(Request)})

    def update(self, Request):
        """ Update Post Controller """

        # Get post via slug
        posts = Post.where('slug', Request.param('slug')).get()

        # Updates Post
        posts[0].title = remove_whitespaces(Request.input('title'))
        posts[0].slug = slugify(posts[0].title)
        posts[0].body = remove_whitespaces(Request.input('body'))
        posts[0].category = remove_whitespaces(Request.input('category'))

        posts[0].save()

        return Request.redirect('dashboard/blog/post/{}/update'.format(posts[0].slug), {'Auth': Auth(Request)})

    def show_delete(self, Request):
        """ Display Post Delete page """

        # Get post via slug
        posts = Post.where('slug', Request.param('slug')).get()

        return view('dashboard/blog/post/delete', {'post': posts[0], 'Auth': Auth(Request)})

    def delete(self, Request):
        """ Delete Post Controller """

        # Get post via slug
        posts = Post.where('slug', Request.param('slug')).get()

        posts[0].delete()

        return Request.redirect('dashboard/blog/main', {'Auth': Auth(Request)})

    def preview(self, Request, RenderEngine):
        """ Display all posts in blog editor """

        # Get post via slug
        posts = Post.where('slug', Request.param('slug')).get()
        posts[0].body = RenderEngine(posts[0].body)

        return view('dashboard/blog/post/preview', {'author': User, 'Auth': Auth(Request),
                                               'posts': posts[0]})

    def activate(self, Request):
        """ Activates post to be displayed """

        # Get post via slug
        posts = Post.where('slug', Request.param('slug')).get()
        posts[0].is_live = 1
        posts[0].save()

        return Request.redirect('dashboard/blog/main', {'Auth': Auth(Request)})

    def deactivate(self, Request):
        """ Removes post from active list """

        # Get post via slug
        posts = Post.where('slug', Request.param('slug')).get()
        posts[0].is_live = 0
        posts[0].save()
        
        return Request.redirect('dashboard/blog/main', {'Auth': Auth(Request)})
