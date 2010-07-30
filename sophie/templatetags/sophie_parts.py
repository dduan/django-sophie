from django import template
from django.core.urlresolvers import reverse

from sophie.utils import multiblog_enabled

register = template.Library()

@register.inclusion_tag('sophie/templatetags/lists_category_of.tag')
def sophie_lists_category_of(blog):
    return {'category_list': blog.get_categories()}

@register.inclusion_tag('sophie/templatetags/shows_feed_of.tag')
def sophie_shows_feed_of(blog):
    return { 'blog': blog }

@register.inclusion_tag('sophie/templatetags/links_siblings_of.tag')
def sophie_links_siblings_of(page, blog, urlname):
    # conditional operatior hack xx and yy or zz == xx ? yy : zz
    url_bits = multiblog_enabled and { 'blog_slug': blog.slug } or {}

    # Note that previous_page_number() is dumb, it returns the number
    # regardless of whether that page exists, same with next_page_number.
    # So, this needs to be guarded in the template
    url_bits['page_num'] = page.previous_page_number()
    previous_link = reverse( urlname, kwargs=url_bits)

    url_bits['page_num'] = page.next_page_number()
    next_link = reverse( urlname, kwargs=url_bits)
    
    return {
        'previous_link': previous_link,
        'next_link': next_link,
        'page': page,
    }

@register.inclusion_tag('sophie/templatetags/lists_entries_in.tag')
def sophie_lists_entries_in(entries, blog, empty_msg = ''):
    return {
        'entries': entries,
        'blog': blog,
        'empty_msg': empty_msg,
    }

