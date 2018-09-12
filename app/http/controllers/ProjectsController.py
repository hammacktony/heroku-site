''' A Module Description '''

class ProjectsController:
    ''' Class Docstring Description '''

    def show(self, Request, Application):
        ''' Show Projects Template '''
        return view('projects', {'app': Application})
