''' A Module Description '''


class VolcanoesController:
    ''' Class Docstring Description '''

    def show(self, Application):
        ''' Show Home Template '''
        return view('projects/volcanoes', {'app': Application}).cache_for(1, 'month')
