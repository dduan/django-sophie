from django import template

register = template.Library()

@register.inclusion_tag('sophie/templatetags/lists_category_of.tag')
def sophie_lists_category_of(blog):
    return {'category_list': blog.get_categories()}
