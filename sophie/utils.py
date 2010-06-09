'''
Utilities for django-sophie
'''

from models import Blog

def get_blog(slug):
    ''' 
    get the blog entity identified by slug, if it doesn't
    exist, get the one with the smallest id
    '''
    try:
        return Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Blog.objects.all()[0]

