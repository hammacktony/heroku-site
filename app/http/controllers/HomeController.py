''' A Module Description '''


class HomeController:
    ''' Class Docstring Description '''

    def show(self, Application):
        ''' Show Index Template '''
        return view('index', {'app': Application})
