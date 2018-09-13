from masonite.provider import ServiceProvider
from dashboard.Link import BaseLink

class HelloWorldLink(BaseLink):
    display = 'Hello World'
    url = '/dashboard/helloworld'


class HelloWorldProvider(ServiceProvider):

    def register(self):
        self.app.bind('HelloWorld', HelloWorldLink)

    def boot(self):
        pass
