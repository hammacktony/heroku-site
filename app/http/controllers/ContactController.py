''' A Module Description '''

import os

class ContactController:
    ''' Class Docstring Description '''

    def show(self, Request, Application):
        ''' Show Contact Template '''
        return view('contact', {'app': Application})

    def store(self, Request, Mail):
        ''' Show Contact Template '''
        name = Request.input('name')
        from_email = Request.input('email')
        body = Request.input('message')
        body = body + f'\n\n\n\n, {name.title()}'
        Mail.subject('User Contact Form from Masonite').send_from(from_email).to("hammack.tony@gmail.com").send(body)
        return Request.redirect('/')