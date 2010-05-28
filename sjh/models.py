from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

class Category(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    slug = models.SlugField(primary_key = True, unique = True)
    blog = models.ForeignKey(Blog)
    count = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.slug
    
    @models.permalink
    def get_absolute_url(self):
        return ('category_view', (), { 'category_slug': self.slug })

class Post(models.Model):
    
    MARKDOWN = 1
    MARKUP_CHOICES = (
            (MARKDOWN, 'Markdown'),
    )

    DRAFT = 0
    PUBLISHED = 1
    HIDDEN = 2
    STATUS_CHOICES = (
            (DRAFT, 'Draft'),
            (PUBLISHED, 'Published'),
            (HIDDEN, 'Hidden'),
    )

    slug = models.SlugField(primary_key = True, uinque = True, 
            max_length = 250)
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    last_update = models.DateTimeField()
    markup = models.PositiveIntegerField(default = MARKDOWN, 
            choices = MARKUP_CHOICES)
    body = models.TextField()
    body_html = models.TextField()
    teaser = models.TextField(blank = True)
    teaser_html = models.TextField(blank = True)
    status = models.PositiveIntegerField(defualt = DRAFT,
            choices = STATUS_CHOICES)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('post_view', (), { 'page_slug': self.slug })
