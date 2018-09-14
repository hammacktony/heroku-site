from masonite.provider import ServiceProvider
from dashboard.Link import BaseLink

class DashboardBlogLink(BaseLink):
    display = 'Blog'
    url = '/dashboard/blog'


class DashboardBlogProvider(ServiceProvider):

    def register(self):
        self.app.bind('Blog', DashboardBlogLink)

    def boot(self):
        pass
