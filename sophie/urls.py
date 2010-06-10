from django.conf.urls.defaults import *
from sophie.models import Blog

# Page urls
urlpatterns = patterns('sophie.views',
    url(r'(?P<blog_slug>)?^$', 'show_index', name='index_view'),
    url(r'^((?P<blog_slug>)/)?entries/$', 'list_entries'),
    url(r'^((?P<blog_slug>)/)?entries/(?P<page_num>\d+)/$', 'list_entries'),
    url(r'^((?P<blog_slug>)/)?category/(?P<category_slug>\w+)/$', 
        'show_category', name='category_view'),
    url(r'^((?P<blog_slug>)/)?category/(?P<category_slug>\w+)/(?P<page_num>\d+)/$', 
        'show_category', name='category_view'),
    # Reserved for future use, held till 0.1.0
    #url(r'^((?P<blog_slug>)/)?tag/(?P<tag_slug>)/$', 'show_tag'),
    #url(r'^((?P<blog_slug>)/)?tag/(?P<tag_slug>)/(?P<page_num>]d+)/$', 'show_tag'),
    #url(r'^((?P<blog_slug>)/)?archive/(?P<year>\d{4})/((?P<month>\d{1,2})/$','show_archive'),
    #url(r'^((?P<blog_slug>)/)?archive/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<page_num>\d+)/$',
    #    'show_archive'),
    url(r'^((?P<blog_slug>)/)?(?P<entry_slug>\w+)/$', 'show_entry', name='entry_view'),
)

# Feed urls
urlpatterns += patterns('sophie.feeds',
    url(r'^((?P<blog_slug>)/)?feed/$', 'BlogFeed', name='blog_feed'),
    url(r'^((?P<blog_slug>)/)?category/(?P<category_slug>\w+)/feed/$', 
        'CategoryFeed', name='blog_feed'),
)

# Sitemap urls

sitemaps = {}

blogs = Blog.objects.all()

for blog in blogs:
    sitemaps[blog.slug] = BlogSitemap(blog)

urlpatterns += patterns(''
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        { 'sitemaps': sitemaps } )
