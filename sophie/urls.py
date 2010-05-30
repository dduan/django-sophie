from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'sophie.views.index', name='index_view'),
    (r'^entries/(?P<page_num>)/$', 'sophie.views.list_entries'),
    (r'^category/(?P<category_slug>\w+)/(?P<page_num>\d+)/$', 
        'sophie.views.show_category', name = 'category_view'),
    # Reserved for future use, held on 0.1.0
    #(r'^tag/(?P<tag_slug>)/(?P<page_num>)/$', 'sophie.views.show_tag'),
    #(r'^archive/(?P<year>)/(?P<month>)/(?P<page_num>)/$',
        'sophie.views.show_archive'),
    (r'^(?P<entry_slug>\w+)/$', 'sophie.views.show_entry', name='entry_view'),
)

