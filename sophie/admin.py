from django.contrib import admin
from sophie.models import Entry, Category, Blog

class EntryAdmin(admin.ModelAdmin):
    save_on_top = True

class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ('count',)

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
