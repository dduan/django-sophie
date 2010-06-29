from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from sophie.utils import get_blog
from sophie.models import Entry, Category

class BaseFeed(Feed):
    ''' 
    Base class for real feeds.

    Used for feeds in which items are Entry instances.
    '''

    def get_object(self, request):
        pass

    def title(self, obj):
        return obj.title

    def description(self, obj):
        return obj.description
    
    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        pass

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        if item.blog.full_entry_in_feed:
            return item.body_html
        else:
            return item.teaser_html

    def item_author_name(self, item):
        return item.author.get_full_name()

class BlogFeed(BaseFeed):
    '''
    Feed for a Blog.
    '''

    def get_object(self, request, blog_slug=None):
        return get_blog(blog_slug)

    def items(self, obj):
        return Entry.live.filter( blog=obj )[:obj.feed_length]

class CategoryFeed(BaseFeed):
    '''
    Feed for a Category.
    '''

    def get_object(self, request, blog_slug=None, category_slug=None):
        return get_object_or_404(Category.objects.get(blog=blog_slug, 
            slug=category_slug))

    def items(self, obj):
        return Entry.live.filter( category=obj )[:obj.blog.feed_length]

