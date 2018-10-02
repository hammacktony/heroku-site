''' A RenderEngine Service Provider '''
from masonite.provider import ServiceProvider

# Render Engine
from mistune import Markdown

class RenderEngineProvider(ServiceProvider):

	wsgi = False

	def register(self):
		''' Registers the Html Render Engine Into The Service Container '''
		self.app.bind('RenderEngine', Markdown())

	def boot(self):
		pass
