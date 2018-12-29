from masonite.provider import ServiceProvider
from dashboard.Link import BaseLink, UserLink


class PersonalBlogLink(BaseLink):
    display = 'Personal Blog'
    url = '/dashboard/blog/personal/home'


class TechBlogLink(BaseLink):
    display = 'Tech Blog'
    url = '/dashboard/blog/tech/home'


class ProfileLink(UserLink):
    display = 'Profile'
    url = '/dashboard/user/profile'

class BlogLinkProvider(ServiceProvider):

    def register(self):
        self.app.bind('PersonalBlog', PersonalBlogLink)
        self.app.bind('TechBlog', TechBlogLink)
        self.app.bind('Profile', ProfileLink)

    def boot(self):
        pass
