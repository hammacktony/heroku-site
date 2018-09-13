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
        Mail.subject('Contact from Masonite').send_from('extra.promotions.th@gmail.com').to("hammack.tony@gmail.com").send("test")
