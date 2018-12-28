''' Sentry Hook Description '''
import os

from raven import Client

client = Client(os.getenv("SENTRY_CLIENT_KEY"))

class SentryHook:
    def __init__(self):
        pass
    
    def load(self, app):
        # client.captureException()
        pass