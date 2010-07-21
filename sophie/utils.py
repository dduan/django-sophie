'''
Utilities for django-sophie
'''

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings

# set multiblog_enabled = True to enable multi blog url routing
multiblog_enabled = getattr(settings, 'SOPHIE_ENABLES_MULTIBLOG', False)

def route_template(basename, extraname):
    ''' 
    Sophie's template locating logic in addition to Django's setting.

    The given basename is looked for in the following order:

        1.  sophie/[blog_slug]/[basename]_[extraname].html
        2.  sophie/[blog_slug]/[basename].html
        3.  sophie/default/[basename]_[extraname].html
        4.  sophie/default/[basename].html

    '''
    pass

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

