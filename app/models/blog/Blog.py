""" Repository for Blog Models """
from .Personal import Personal
from .Tech import Tech

class Blog:
    
    blogs = {
        'personal': Personal,
        'tech': Tech
    } 

    def make(self, blog):
        """ Return Blog """

        return self.blogs[blog]
