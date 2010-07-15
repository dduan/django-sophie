from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

import datetime

from sophie.managers import LiveEntryManager, ShownCategoryManager
from sophie.utils import multiblog_enabled


class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    slug = models.SlugField()
    entry_per_page = models.PositiveIntegerField(default = 5)
    feed_length = models.PositiveIntegerField(default = 15)
    feed_service = models.CharField(max_length=200, blank=True)
    highlight_code = models.BooleanField(default = True)
    full_entry_in_page = models.BooleanField(default = True)
    full_entry_in_feed = models.BooleanField(default = True)
    g_analytics_tracking_id = models.CharField(max_length=50, blank=True)
    disqus_shortname = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        c = {}
        if multiblog_enabled:
            c.update({ 'blog_slug': self.slug })
        return ('index_view', (), c)

    @models.permalink
    def get_original_feed(self):
        c = {}
        if multiblog_enabled:
            c.update({ 'blog_slug': self.slug })
        return ('blog_feed', (), c)

    def get_feed(self):
        if self.feed_service:
            return self.feed_service
        else:
            return self.get_original_feed()

    def get_categories(self):
        return Category.visible.filter(blog=self)
    
    def get_entries(self):
        return Entry.live.filter(blog=self)

    @classmethod
    def get_blog(cls, slug=None):
        ''' 
        if multiblog_enabled is True, then this function gets the blog 
        entity identified by slug. if slug isn't given, it tries to give the 
        instance with minimal id.
        '''
        if slug == None:
            try:
                return cls.objects.all()[0]
            except IndexError:
                b = cls( title = 'Sophie Blog', slug = 'default' )
                b.save()
                return b
        elif multiblog_enabled:
            return get_object_or_404(cls, slug=slug)

class Category(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    slug = models.SlugField(unique = True)
    blog = models.ForeignKey(Blog)
    count = models.IntegerField(default = 0)
    shown = models.BooleanField(default = True)

    objects = models.Manager()
    visible = ShownCategoryManager()

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        c = { 
                'category_slug': self.slug
            }
        if multiblog_enabled:
            c.update({'blog_slug': self.blog.slug})
        return ('category_view', (), c)

    def get_entries(self):
        return Entry.live.filter(category=self)

class Entry(models.Model):
    
    HTML_SYNTAX = 0
    MARKDOWN_SYNTAX = 1
    MARKUP_CHOICES = (
            (HTML_SYNTAX, 'Html'),
            (MARKDOWN_SYNTAX, 'Markdown'),
    )

    DRAFT_STATUS = 0
    LIVE_STATUS = 1
    HIDDEN_STATUS = 2
    STATUS_CHOICES = (
            (DRAFT_STATUS, 'Draft'),
            (LIVE_STATUS, 'Live'),
            (HIDDEN_STATUS, 'Hidden'),
    )

    category = models.ForeignKey(Category)
    blog = models.ForeignKey(Blog, editable = False)
    slug = models.SlugField(unique = True, max_length = 250)
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField(default = datetime.datetime.now)
    last_update = models.DateTimeField(editable = False)
    markup = models.PositiveIntegerField(default = MARKDOWN_SYNTAX, 
            choices = MARKUP_CHOICES)
    body = models.TextField(blank = True)
    body_html = models.TextField(blank = True, editable = False)
    teaser = models.TextField(blank = True)
    teaser_html = models.TextField(blank = True, editable = False)
    status = models.PositiveIntegerField(default = DRAFT_STATUS,
            choices = STATUS_CHOICES)
    author = models.ForeignKey(User)

    objects = models.Manager()
    live = LiveEntryManager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        c = { 
                'entry_slug': self.slug
            }
        if multiblog_enabled:
            c.update({'blog_slug': self.blog.slug})
        return ('entry_view', (), c)

    def save(self, *args, **kwargs):
        """ convert markup to html, book-keep category counter """ 

        if not self.id: # newly created
            self.pub_date = datetime.datetime.now()
            self.category.count = self.category.count + 1
            self.category.save()

        self.last_update = datetime.datetime.now()
        self.blog = self.category.blog
        self.apply_markup()

        super(Entry, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ counter-method of self.save, book-keeping category counter """

        self.category.count = self.category.count - 1
        self.category.save()

        super(Entry, self).delete(*args, **kwargs)
    
    def apply_markup(self):
        """
        Find markup method (do_markup) according to self.markup;
        Determine whether to highlight the code inside the markup;
        And finally apply the markup
        """

        if self.markup == self.MARKDOWN_SYNTAX:
            from functools import partial
            import markdown

            # warning, here's a conditional operator hack
            do_markup = partial(markdown.markdown, 
                    extensions = self.blog.highlight_code and ['codehilite'] or [])
        else: # default to HTML_SYNTAX, do nothing
            do_markup = lambda x: x
        
        self.body_html = do_markup(self.body)
        if self.teaser:
            self.teaser_html = do_markup(self.teaser)
