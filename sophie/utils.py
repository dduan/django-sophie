'''
Utilities for django-sophie
'''

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings

# set multiblog_enabled = True to enable multi blog url routing
if hasattr(settings, 'SOPHIE_ENABLES_MULTIBLOG'):
    multiblog_enabled =  settings.SOPHIE_ENABLES_MULTIBLOG
else:
    multiblog_enabled = False

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

