from django.conf.urls.defaults import *

from sophie.models import Blog
from sophie.sitemaps import BlogSitemap
from sophie.feeds import BlogFeed, CategoryFeed

# To save some typing later...
blog_bit = r'(?:(?P<blog_slug>[\w-]+)/)?'
page_bit = r'(?:(?P<page_num>\d+)/)?'
slug_bit = r'(?P<%s_slug>[\w-]+)'

# Feed urls
urlpatterns = patterns('',
    url(r'^%sfeed/$' % (blog_bit), BlogFeed(), name='blog_feed'),
    url(r'^%scategory/%s/feed/$' % (blog_bit, slug_bit % 'category'), 
        CategoryFeed(), name='category_feed'
    ),
)

# Sitemap urls

sitemaps = {}

blogs = Blog.objects.all()

for blog in blogs:
    sitemaps[blog.slug] = BlogSitemap(blog)

urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', 
        { 'sitemaps': sitemaps } ),
    (r'sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap',
        { 'sitemaps': sitemaps } ),
)

# Page url

urlpatterns += patterns('sophie.views',
    url(r'^%sentries/%s$' % (blog_bit, page_bit), 'list_entries', 
        name="entry_list_view"),
    url(r'^%scategory/%s/%s$' %(blog_bit, slug_bit%'category', page_bit), 
        'show_category', name='category_view'),
    # Reserved for future use, held till 0.1.0
    #url(r'%stag/%s/%s$' % (blog_bit, slug_bit % 'tag', page_bit), 
    #    'show_tag', name='tag_view'),
    #url(r'^%sarchive/(?P<year>\d{4})/(?P<month>\d{1,2})/$'%(blog_bit,page_bit),
    #    'show_archive', name='monthly_archive_view'),
    url(r'^%sentry/%s/$' % (blog_bit, slug_bit % 'entry'), 
        'show_entry', name='entry_view'),
    url(r'^%s$' % blog_bit, 'show_index', name='index_view'),
)

