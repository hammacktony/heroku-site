''' A Controller for Live Posts'''
from app.User import User
from lib.helpers.PostsHelpers import convert_slug_to_category
from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View
from app.models.blog import Blog
from mistune import Markdown


class PostsController:
    ''' Posts Controller '''

    def __init__(self, request: Request):
        """ Set blog table at runtime """
        self.blog_name = request.param('blog').lower()
        self.Blog = Blog().make(self.blog_name)

    def show_all(self, view: View):
        """ Controller to show all posts"""
        # dd(self.Blog)
        posts = self.Blog.where('is_live', 1).order_by(
            'updated_at', 'desc').get()
        return view.render('blog', {'author': User, 'posts': posts, 'blog': self.blog_name})

    def show_one(self, request: Request, markdown: Markdown, view: View):
        """ Controller to show single post"""

        # Get post via slug
        posts = self.Blog.where('slug', request.param('slug')
                                ).where('is_live', 1).get()

        # Render blog content
        posts[0].body = markdown(posts[0].body)

        # Get current author
        user = User.where('id', posts[0].author_id).get()

        # Get recent posts
        recent_posts = self.Blog.where('is_live', 1).order_by(
            'updated_at', 'desc').take(5).get()

        return view.render('blog/post', {'user': user[0], 'post': posts[0], 'recent': recent_posts, 'blog': self.blog_name})

    def show_category(self, request: Request, view: View):
        """ Controller to show posts by category"""

        category = convert_slug_to_category(request.param('category'))
        posts = self.Blog.where('category', category).where('is_live', 1).order_by(
            'updated_at', 'desc').get()

        return view.render('blog/category', {'author': User, 'category': category, 'posts': posts, 'blog': self.blog_name})

    def show_author(self, request: Request, view: View):
        """ Controller to show posts by author"""

        author = User.where('user_name', request.param('author')).get()

        posts = self.Blog.where('author_id', author[0].id).where('is_live', 1).order_by(
            'created_at', 'desc').get()

        return view.render('blog/author', {'author': author[0], 'posts': posts, 'blog': self.blog_name})
