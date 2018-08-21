''' A Module Description '''


class VolcanoesController:
    ''' Class Docstring Description '''

    def show(self, Application):
        ''' Show Home Template '''
        return view('projects/volcano', {'app': Application})
