from django.template import RequestContext

from django.http import HttpResponse
from django.shortcuts import  get_object_or_404
from sophie.models import Blog, Category, Entry
from sophie.utils import LaidbackPaginator, multiblog_enabled, route_template


def list_entries( request, blog_slug=None, page_num=1 ):
    ''' renders requested page, a list of date-ordred entries '''
    blog = Blog.get_blog(blog_slug)
    pages = LaidbackPaginator(blog.get_entries(), blog.page_length)
    template, template_dir = route_template('entry_list', blog_slug=blog.slug)
    return HttpResponse(template.render( 
        RequestContext(request, { 
            'blog': blog,
            'page': pages.page(page_num),
            'multiblog': multiblog_enabled,
            'base_template': '%s/base.html' % template_dir,
            'sidebar_template': '%s/sidebar.html' % template_dir,
        })
    ))

def show_index(request, blog_slug=None):
    ''' renders index page'''
    return list_entries(request, blog_slug)

def show_category(request, blog_slug=None, category_slug=None, page_num=1):
    ''' lists entries under category specified by category_slug '''
    blog = Blog.get_blog(blog_slug)
    category = get_object_or_404(Category, blog=blog, slug=category_slug)
    entries = Entry.live.filter( category=category )
    pages = LaidbackPaginator(entries, blog.page_length)
    template, template_dir = route_template(
        'category_details', 
        blog_slug=blog.slug
    )
    return HttpResponse(template.render(
        RequestContext(request, { 
            'blog': blog,
            'category': category,
            'page': pages.page(page_num),
            'multiblog': multiblog_enabled,
            'base_template': '%s/base.html' % template_dir,
            'sidebar_template': '%s/sidebar.html' % template_dir,
        })
    ))

def show_entry(request, entry_slug, blog_slug=None):
    blog = Blog.get_blog(blog_slug)
    entry = get_object_or_404(Entry, slug=entry_slug)
    template, template_dir = route_template(
        'entry_details', 
        blog_slug=blog.slug
    )
    return HttpResponse(template.render(
        RequestContext(request, {
            'blog': blog,
            'entry': entry,
            'multiblog': multiblog_enabled,
            'base_template': '%s/base.html' % template_dir,
            'sidebar_template': '%s/sidebar.html' % template_dir,
        })
    ))

