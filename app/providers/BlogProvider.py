from masonite.provider import ServiceProvider
from dashboard.Link import BaseLink, UserLink

class BlogEditorLink(BaseLink):
    display = 'Blog'
    url = '/dashboard/blog/main'

class ProfileLink(UserLink):
    display = 'Profile'
    url = '/dashboard/user/profile'

# class ManagementLink(UserLink):
#     display = 'Profile'
#     url = '/dashboard/profile'

class BlogProvider(ServiceProvider):
	
    def register(self):
        self.app.bind('BlogEditor', BlogEditorLink)
        self.app.bind('Profile', ProfileLink)

    def boot(self):
        pass