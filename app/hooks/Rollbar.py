''' Rollbar Hook Description '''
import os
import rollbar

rollbar.init(os.getenv("ROLLBAR_POST_SERVER_ITEM_ACCESS_TOKEN"))

class RollbarHook:
    def __init__(self):
        pass
    
    def load(self, app):
        # rollbar.report_exc_info()
        pass