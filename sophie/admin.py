from django.contrib import admin
from sophie.models import Entry, Category, Blog

class EntryAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('count',)

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
