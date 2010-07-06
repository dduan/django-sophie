'''
Utilities for django-sophie
'''

from models import Blog
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage

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

class LaidbackPaginator(Paginator):
    '''
    Overwrites the original page method so it could be more
    tolerant to invalid page number.
    '''
    def page(self, number):
        '''
        If number is a invalid integer, return page 1.
        If number exceed the max page number, return the last page.
        '''
        try:
            n = int(number)
        except (ValueError, TypeError):
            n = 1

        try:
            return super(LaidbackPaginator, self).page(n)
        except (EmptyPage, InvalidPage):
            return super(LaidbackPaginator, self).page(self.num_pages)

