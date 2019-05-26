''' Contact Page Controller '''

import os
from masonite.view import View
from masonite.request import Request
from masonite import Mail


class ContactController:
    ''' Controller for Contact Page '''

    def show(self, request: Request, view: View):
        ''' Show Contact Template '''
        return view.render('contact', {
            'app': request.app().make('Application')
        }).cache_for(1, 'month')

    def store(self, request: Request, mail: Mail):
        ''' Show Contact Template '''
        name = request.input('name')
        from_email = request.input('email')
        body = request.input('message')
        body = body + f'\n\n\n\n, {name.title()}'
        mail.subject('User Contact Form from Masonite').queue().send_from(from_email).to("hammack.tony@gmail.com").send(body)
        return request.redirect('/')