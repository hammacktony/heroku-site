''' A HookProvider Service Provider '''
from masonite.provider import ServiceProvider
from ..hooks.sentry import SentryHook

class SentryServiceProvider(ServiceProvider):
    def register(self):
        self.app.bind('SentryExceptionHook', SentryHook())
        
    def boot(self):
        pass
