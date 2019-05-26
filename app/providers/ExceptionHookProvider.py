''' A HookProvider Service Provider '''
from masonite.provider import ServiceProvider
from app.hooks.Sentry import SentryHook

class ExceptionHookServiceProvider(ServiceProvider):
    def register(self):
        self.app.bind('SentryExceptionHook', SentryHook())
        
    def boot(self):
        pass
