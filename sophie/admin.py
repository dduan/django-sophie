from django.contrib import admin
from sophie.models import Entry, Category, Blog

def delete_selected_action(modeladmin, request, queryset):
    """
    A general action to replace the default 'delete selected objects'
    action in contrib.admin, which does not call obj.delete thus not
    behave as expected
    """
    for obj in queryset:
        obj.delete()
delete_selected_action.short_description = "Delete Selected Items"

def make_entry_live_action(modeladmin, request, queryset):
    queryset.update( status = Entry.LIVE_STATUS )
make_entry_live_action.short_description = "Make Selected Entries Live"

def make_entry_hidden_action(modeladmin, request, queryset):
    queryset.update( status = Entry.HIDDEN_STATUS )
make_entry_hidden_action.short_description = "Make Selected Entries Hidden"

def make_entry_draft_action(modeladmin, request, queryset):
    queryset.update( status = Entry.DRAFT_STATUS )
make_entry_draft_action.short_description = "Make Selected Entries Drafts"

class EntryAdmin(admin.ModelAdmin):

    save_on_top = True

    actions = (
            delete_selected_action,
            make_entry_live_action,
            make_entry_hidden_action,
            make_entry_draft_action,
            )

    prepopulated_fields = { 'slug': ('title',) }

    radio_fields = { 'status': admin.HORIZONTAL }
    fieldsets = (
        ('Entry Content', {
            'fields': (
                ('category', 'author', 'markup'),
                ('title', 'slug'),  
                'body', 
                'teaser',
                'pub_date',
            ) 
        }),
        ('Entry Settings', {
            'fields': ( 
                'status',
                'allow_comment',
            ),
        }),
    )

    def get_actions(self, request):
        actions = super(EntryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ('count',)
    prepopulated_fields = {'slug': ('title',)}

class BlogAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Infomation', {
            'fields': (
                ('title', 'slug'),
                'description',
            ),
        }),
        ('Entry Settings', {
            'fields': (
                'full_entry_in_page',
                'highlight_code',
                'page_length',
            ),
            'classes': ('collapse',)
        }),
        ('Feed Settings', {
            'fields': (
                'full_entry_in_feed',
                'feed_length', 
                'feed_service'
            ),
            'classes': ('collapse',)
        }),
        ('Services', {
            'fields': (
                'g_analytics_tracking_id',
                'disqus_shortname',
            ),
            'classes': ('collapse',)
        }),
    )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
