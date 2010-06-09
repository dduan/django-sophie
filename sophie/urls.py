from django.conf.urls.defaults import *

# Page urls
urlpatterns = patterns('sophie.views',
    url(r'^$', 'show_index', name='index_view'),
    url(r'^entries/$', 'list_entries'),
    url(r'^entries/(?P<page_num>\d+)/$', 'list_entries'),
    url(r'^category/(?P<category_slug>\w+)/$', 
        'show_category', name='category_view'),
    url(r'^category/(?P<category_slug>\w+)/(?P<page_num>\d+)/$', 
        'show_category', name='category_view'),
    # Reserved for future use, held till 0.1.0
    #url(r'^tag/(?P<tag_slug>)/$', 'show_tag'),
    #url(r'^tag/(?P<tag_slug>)/(?P<page_num>]d+)/$', 'show_tag'),
    #url(r'^archive/(?P<year>\d{4})/((?P<month>\d{1,2})/$','show_archive'),
    #url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<page_num>\d+)/$',
    #    'show_archive'),
    url(r'^(?P<entry_slug>\w+)/$', 'show_entry', name='entry_view'),
)

# Feed urls
urlpatterns+ = patterns('sophie.feeds',
    url(r'^feed/$', 'BlogFeed', name='blog_feed'),
    url(r'^category/(?P<category_slug>\w+)/feed/$', 
        'CategoryFeed', name='blog_feed'),
)
