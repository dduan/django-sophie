from django.test import TestCase
from django.contrib.auth.models import User
from sophie.models import Blog, Category, Entry

class EntrySaveTest(TestCase):
    def setUp(self):
        self.user = User(username='DaN',password='DaN@gmail.com')
        self.user.save()
        self.blog = Blog(
            title = "Test Blog",
            slug = "test-blog",
            description = "Testing is cool",
        )
        self.blog.save()
        self.category = Category(
                title = "Test Category",
                slug = "test-category",
                blog = self.blog
        )
        self.category.save()
        self.entry = Entry(
                category = self.category,
                blog = self.blog,
                slug = "test-entry",
                title = "test entry",
                author = self.user,
                body = 'code goes like this:\n\n'
                    '    #!python \n'
                    '    from django import http \n'
                )
        self.target_body = u'<p>code goes like this:</p>\n<table class="codehilitetable"><tr><td class="linenos"><div class="linenodiv"><pre>1</pre></div></td><td class="code"><div class="codehilite"><pre><span class="kn">from</span> <span class="nn">django</span> <span class="kn">import</span> <span class="n">http</span>\n</pre></div>\n</td></tr></table>'
        self.entry.save()

    def test_that_markdown_works(self):
        self.failUnlessEqual(self.entry.body_html, self.target_body)

