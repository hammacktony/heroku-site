''' A Module Description '''
from app.models.Post import Post
from masonite.facades.Auth import Auth


class PostController:
    ''' Class Docstring Description '''

    def show(self, Request, Application):
        posts = Post.all()
        return view('blog/posts', {'app': Application, 'Auth': Auth(Request), 'posts': posts})

    def single(self, Request, Application):
        post = Post.find(request().param('id'))
        return view('blog/single', {'app': Application, 'Auth': Auth(Request), 'post': post})

    def update(self, Request, Application):
        post = Post.find(request().param('id'))
        return view('blog/update', {'app': Application, 'Auth': Auth(Request),'post': post})

    def store(self, Request, Application):
        post = Post.find(request().param('id'))
    
        post.title = request().input('title')
        post.body = request().input('body')
    
        post.save()
    
        return 'post updated'

    def delete(self, Request, Application):
        post = Post.find(request().param('id'))
    
        post.delete()

        return 'post deleted'