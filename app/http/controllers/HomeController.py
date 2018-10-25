''' A Module Description '''
from app.User import User
from masonite.facades.Auth import Auth

class HomeController:
    ''' Class Docstring Description '''

    def show(self):
        ''' Show Index Template '''
        
        # Get my identity
        user = User.where('id', '1').get()
        
        return view('index', {'user': user[0]})
