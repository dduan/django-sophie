'''
Utilities for django-sophie
'''

from models import Blog
from django.shortcuts import get_object_or_404

def get_blog(slug):
    ''' 
    gets the blog entity identified by slug. 
    if slug isn't given, give the instance with minimal id.
    404 if not found.
    '''
    if slug == None:
        return Blog.objects.all()[0]
    else:
        return get_object_or_404(Blog, slug=slug)

