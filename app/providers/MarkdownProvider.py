''' A Markdown Service Provider '''
from masonite.provider import ServiceProvider

# Render Engine
from mistune import Markdown


class MarkdownProvider(ServiceProvider):

    wsgi = False

    def register(self):
        ''' Registers Markdown Renderer Into The Service Container '''
        self.app.bind('Markdown', Markdown())

    def boot(self):
        pass
