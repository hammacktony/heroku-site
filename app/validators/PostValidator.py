""" Validate Incoming Posts """
from masonite.validator import Validator
from validator import Pattern, Required


class PostValidator(Validator):

    def register_form(self):

        self.validate({
            'title': [Required, Pattern('.*\S+.*')],
            'body': [Required],
            'category': [Pattern('.*\S+.*')],
        })

        self.messages({
            'title': 'Title Must Be Present',
            'body': 'Body Must Be Present'
        })
