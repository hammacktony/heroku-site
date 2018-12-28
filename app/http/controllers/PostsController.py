''' A Controller for Live Posts'''
from app.Post import Post
from app.User import User
from helpers.PostsHelpers import convert_slug_to_category
from masonite.facades.Auth import Auth


class PostsController(object):
    ''' Posts Controller '''

    def __init__(self, Request):
        """ Set blog table at runtime """
        self.name = Request.param('blog')

    def show_all(self, BlogRepo):
        """ Controller to show all posts"""
        Blog = BlogRepo.get(self.name)
        # dd(Blog)
        posts = Blog.where('is_live', 1).get()
        return view('blog', {'author': User, 'posts': posts})

    def show_one(self, Request, RenderEngine):
        """ Controller to show single post"""

        # Get post via slug
        posts = Post.where('slug', Request.param('slug')
                           ).where('is_live', 1).get()

        # Render blog content
        posts[0].body = RenderEngine(posts[0].body)

        # Get current author
        user = User.where('id', posts[0].author_id).get()

        # Get recent posts
        recent_posts = Post.where('is_live', 1).order_by(
            'created_at', 'desc').take(5).get()

        return view('blog/post', {'user': user[0], 'post': posts[0], 'recent': recent_posts})

    def show_category(self, Request):
        """ Controller to show posts by category"""

        category = convert_slug_to_category(Request.param('category'))
        posts = Post.where('category', category).where('is_live', 1).get()

        return view('blog/category', {'author': User, 'category': category, 'posts': posts})

    def show_author(self, Request):
        """ Controller to show posts by author"""

        author = User.where('user_name', Request.param('author')).get()

        posts = Post.where('author_id', author[0].id).where('is_live', 1).get()

        return view('blog/author', {'author': author[0], 'posts': posts})
