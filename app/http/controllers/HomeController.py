''' A Module Description '''
from masonite.facades.Auth import Auth

class HomeController:
    ''' Class Docstring Description '''

    def show(self, Request, Application):
        ''' Show Index Template '''
        return view('index', {'app': Application}).cache_for(1, 'month')
