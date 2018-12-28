''' A HookProvider Service Provider '''
from masonite.provider import ServiceProvider
from app.hooks.Sentry import SentryHook
from app.hooks.Rollbar import RollbarHook

class ExceptionHookServiceProvider(ServiceProvider):
    def register(self):
        self.app.bind('SentryExceptionHook', SentryHook())
        self.app.bind('RollbarExceptionHook', RollbarHook())
        
    def boot(self):
        pass
