from django.db import models
from django.contrib.auth.models import User
import datetime
import markdown

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

class Category(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    slug = models.SlugField(primary_key = True, unique = True)
    blog = models.ForeignKey(Blog)
    count = models.IntegerField(default = 0)
    shown = models.BooleanField(defualt = True)

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

    DRAFT = 0
    PUBLISHED = 1
    HIDDEN = 2
    STATUS_CHOICES = (
            (DRAFT_STATUS, 'Draft'),
            (LIVE_STATUS, 'Live'),
            (HIDDEN_STATUS, 'Hidden'),
    )

    slug = models.SlugField(uinque = True, max_length = 250)
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField(default = datetime.datetime.now)
    last_update = models.DateTimeField()
    markup = models.PositiveIntegerField(default = MARKDOWN, 
            choices = MARKUP_CHOICES)
    body = models.TextField(blank = True)
    body_html = models.TextField(blank = True)
    teaser = models.TextField(blank = True)
    teaser_html = models.TextField(blank = True)
    status = models.PositiveIntegerField(defualt = DRAFT,
            choices = STATUS_CHOICES)
    author = models.ForeignKey(User)

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

        self.last_updated = datetime.datetime.now()
        self.body_html = markdown.markdown(self.body, ['codehilite'])

        if self.teaser:
            self.teaser_html = markdown.markdown(self.teaser, ['codehilite'])

        super(Entry, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ counter-method of self.save, book-keeping category counter """

        self.category.count = self.category.count - 1
        self.category.save()

        super(Entry, self).delete(*args, **kwargs)