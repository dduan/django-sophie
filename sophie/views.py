from django.conf import settings
from django.template import RequestContext

from django.shortcuts import render_to_response, get_object_or_404
from sophie.models import Category, Entry
from sophie.utils import get_blog, LaidbackPaginator


def list_entries(request, 
        blog_slug=None, 
        page_num=1, 
        template='sophie/entry_list.html'):
    ''' renders requested page, a list of date-ordred entries '''
    blog = get_blog(blog_slug)
    pages = LaidbackPaginator(blog.get_entries(), blog.entry_per_page)
    return render_to_response(template, 
        { 
            'blog': blog,
            'page': pages.page(page_num),
        },
        RequestContext(request)
    )

def show_index(request, blog_slug=None):
    ''' renders index page'''
    return list_entries(request, blog_slug)

def show_category(request, 
        blog_slug=None, 
        category_slug=None, 
        page_num=1,
        template = 'sophie/category_details.html'):
    ''' lists entries under category specified by category_slug '''
    blog = get_blog(blog_slug)
    category = get_object_or_404(Category, blog=blog, slug=category_slug)
    entries = Entry.live.filter( category=category )
    pages = LaidbackPaginator(entries, blog.entry_per_page)
    return render_to_response(template, 
        { 
            'blog': blog,
            'category': category,
            'page': pages.page(page_num),
        },
        RequestContext(request)
    )

def show_entry(request, 
        entry_slug, 
        blog_slug=None,
        template = 'sophie/entry_details.html'):
    blog = get_blog(blog_slug)
    entry = get_object_or_404(Entry, slug=entry_slug)
    return render_to_response(template, 
        { 
            'blog': blog,
            'entry': entry,
        },
        RequestContext(request)
    )

