from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'sjh.views.index', name='index_view'),
    (r'^page/(?P<page_num>\d+)/$', 'sjh.views.show_page', name='page_view'),
    (r'^category/(?P<category_slug>\w+)/(?P<page_num>\d+)/$', 
        'sjh.views.show_category', name = 'category_view'),
    (r'^(?P<post_slug>\w+)/$', 'sjh.views.show_post', name='post_view'),
)
