from django.db import models
from django.contrib.auth.models import User
from managers import LiveEntryManager
import datetime
import markdown

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    slug = models.SlugField()
    entry_per_page = models.PositiveIntegerField(default = 5)
    feed_length = models.PositiveIntegerField(default = 15)
    full_entry_on_page = models.BooleanField(default = True)
    full_entry_on_feed = models.BooleanField(default = True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    slug = models.SlugField(unique = True)
    blog = models.ForeignKey(Blog)
    count = models.IntegerField(default = 0, editable = False)
    shown = models.BooleanField(default = True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('category_view', (), { 'category_slug': self.slug })

class Entry(models.Model):
    
    MARKDOWN = 1
    MARKUP_CHOICES = (
            (MARKDOWN, 'Markdown'),
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
    markup = models.PositiveIntegerField(default = MARKDOWN, 
            choices = MARKUP_CHOICES)
    body = models.TextField(blank = True)
    body_html = models.TextField(blank = True, editable = False)
    teaser = models.TextField(blank = True)
    teaser_html = models.TextField(blank = True, editable = False)
    status = models.PositiveIntegerField(default = DRAFT_STATUS,
            choices = STATUS_CHOICES)

    live = LiveEntryManager()
    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post_view', (), { 'page_slug': self.slug })

    def save(self, *args, **kwargs):
        """ convert markup to html, book-keep category counter """ 

        if not self.id: # newly created
            self.pub_date = datetime.datetime.now()
            self.category.count = self.category.count + 1
            self.category.save()

        self.last_update = datetime.datetime.now()
        self.body_html = markdown.markdown(self.body, ['codehilite'])
        self.blog = category.blog

        if self.teaser:
            self.teaser_html = markdown.markdown(self.teaser, ['codehilite'])

        super(Entry, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ counter-method of self.save, book-keeping category counter """

        self.category.count = self.category.count - 1
        self.category.save()

        super(Entry, self).delete(*args, **kwargs)
