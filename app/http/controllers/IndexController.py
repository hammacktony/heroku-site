""" Main page """

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller


class IndexController(Controller):
    def show(self, view: View, request: Request):
        """Show the site."""
        return view.render("app/dist/app/index")
