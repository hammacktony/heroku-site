"""A FeedController Module"""

class FeedController:
    """ Create XML Feeds for Blogs """

    def __init__(self, Request, BlogRepo):
        self.blog_name = Request.param('blog').lower()
        self.Blog = BlogRepo.get(self.blog_name)

    def show(self, Request):

        posts = self.Blog.order_by(
            'created_at', 'desc').get()
        Request.header('Content-Type', 'application/xml', http_prefix=None)

        return view('feed/blog.xml', {'posts': posts, "blog_name": self.blog_name, })