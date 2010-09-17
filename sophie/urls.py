'''
URLs are named following this convention:

    sophie_[part name]_[page type]_url

Where the page type is 'details', there shoudl be a '[part name]_slug' field.
'''

from django.conf.urls.defaults import *

from sophie.models import Blog
from sophie.sitemaps import BlogSitemap
from sophie.feeds import BlogFeed, CategoryFeed
from sophie.utils import multiblog_enabled, blog_bit, page_bit

# This is here to save some typings later..
slug_bit = r'(?P<%s_slug>[\w-]+)'

urlpatterns = patterns('',)

from sophie.plugins import URLStructure

for struct in URLStructure.plugins:
    urlpatterns += struct.get_patterns()
    

# Feed urls
urlpatterns += patterns('',
    url(r'^%sfeed/$' % (blog_bit), BlogFeed(), name='sophie_blog_feed_url'),
    url(r'^%scategory/%s/feed/$' % (blog_bit, slug_bit % 'category'), 
        CategoryFeed(), name='sophie_category_feed_url'
    ),
)

# Sitemap urls

sitemaps = {}

blogs = Blog.objects.all()

for blog in blogs:
    sitemaps[blog.slug] = BlogSitemap(blog)

if multiblog_enabled:
    urlpatterns += patterns('',
        (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', 
            { 'sitemaps': sitemaps } ),
        (r'(?P<section>.+)/sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
            { 'sitemaps': sitemaps } ),
    )
else:
    urlpatterns += patterns('',
        (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
            { 'sitemaps': sitemaps } ),
    )

# Page url

urlpatterns += patterns('sophie.views',
    url(r'^%sentries/%s$' % (blog_bit, page_bit), 'list_entries', 
        name="sophie_entry_list_url"),
    url(r'^%scategory/%s/%s$' %(blog_bit, slug_bit%'category', page_bit), 
        'show_category', name='sophie_category_details_url'),
    # Reserved for future use, held till 0.1.0
    #url(r'%stag/%s/%s$' % (blog_bit, slug_bit % 'tag', page_bit), 
    #    'show_tag', name='sophie_tag_details_url'),
    #url(r'^%sarchive/(?P<year>\d{4})/(?P<month>\d{1,2})/$'%(blog_bit,page_bit),
    #    'show_archive', name='sophie_monthly_details_url'),
    url(r'^%sentry/%s/$' % (blog_bit, slug_bit % 'entry'), 
        'show_entry', name='sophie_entry_details_url'),
    url(r'^%s$' % blog_bit, 'show_index', name='sophie_blog_index_url'),
)

