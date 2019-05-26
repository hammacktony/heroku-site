"""The HomeController Module."""

from app.User import User
from masonite.view import View


class HomeController:
    ''' Class Docstring Description '''

    def show(self, view: View):
        ''' Show Index Template '''
        
        # Get my identity
        user = User.where('id', '1').get()
        
        return view.render('index', {'user': user[0]})
