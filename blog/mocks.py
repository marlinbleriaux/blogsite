from django.http import Http404

class Post():


    POSTS =[
        { 'id': 1, 'title': 'first Post',  'body': 'this is my first post'},
        { 'id': 2, 'title': 'second Post',  'body': 'this is my second post'},
        { 'id': 3, 'title': 'third Post',  'body': 'this is my third post'},
    
    ]
     
    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls, id): 
        try:
            return cls.POSTS[int (id) - 1]  
        except :
            raise Http404('sorry the post #{} was not exist.'.format(id))
          