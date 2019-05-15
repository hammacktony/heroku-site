"""A IndexController Module."""

from masonite.request import Request
from masonite.view import View

class IndexController:
    """IndexController Controller Class."""
    
    def __init__(self, request: Request):
        """IndexController Initializer
        
        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render("index")