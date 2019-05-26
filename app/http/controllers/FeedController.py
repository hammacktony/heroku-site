"""A FeedController Module"""
from masonite.request import Request
from masonite.view import View

from mistune import Markdown
from app.models.blog import Blog

class FeedController:
    """ Create XML Feeds for Blogs """

    def __init__(self, request: Request):
        self.blog_name = request.param('blog').lower()
        self.Blog = Blog.make(self.blog_name)

    def show(self, request: Request, markdown: Markdown, view: View):
        """ Show XML Feed """

        posts = self.Blog.order_by(
            'created_at', 'desc').get()

        # Render Markdown
        for post in posts:
            post.body = markdown(post.body)

        request.header('Content-Type', 'application/xml', http_prefix=None)

        return view.render('feed/blog.xml', {'posts': posts, "blog_name": self.blog_name})