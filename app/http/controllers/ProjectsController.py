''' A Module Description '''

class ProjectsController:
    ''' Class Docstring Description '''

    def show(self, Request, Application):
        ''' Show Projects Template '''
        return view('projects/index', {'app': Application}).cache_for(10, 'days')
