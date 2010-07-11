from django.db import models

class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(
                status=self.model.LIVE_STATUS)

class ShownCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ShownCategoryManager, self).get_query_set().filter(
                shown=True)

#class BlogCategoryManager(models.Manager):
#    def get_query_set(self):
#        return super(BlogCategoryManager, self).get_query_set().filter(
#                blog = self.model.blog.id)
