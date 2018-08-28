''' A Module Description '''
from app.Post import Post
from masonite.facades.Auth import Auth


class BlogController:
    ''' Class Docstring Description '''

    def show(self, Request, Application):
        if not Auth(Request).user():
            Request.redirect('/login')
        return view('blog/blog', {'app': Application, 'Auth': Auth(Request)})

    def store(self, Request):
        Post.create(
            title=Request.input('title'),
            body=Request.input('body'),
            author_id=Request.user().id
        )
        return 'post created'
