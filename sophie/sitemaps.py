from django.contrib.sitemaps import Sitemap
from sophie.models import Entry

class BlogSitemap(Sitemap):
    " sitemap section for a blog "
    changefreq = "monthly"
    priority = 1.0

    def __init__(self, blog):
        " here blog is a Sophie.Blog instance "
        self.blog = blog
        super(BlogSitemap, self).__init__()

    def items(self):
        return Entry.live.filter( blog = self.blog )

    def lastmod(self, obj):
        return obj.last_update
