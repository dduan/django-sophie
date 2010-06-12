from django.shortcuts import render_to_response, get_object_or_404
from sophie.models import Blog, Category, Entry
from sophie.utils import get_blog, LaidbackPaginator
import logging

def list_entries(request, blog_slug=None, page_num=1):
    ''' renders requested page, a list of date-ordred entries '''
    blog = get_blog(blog_slug)

    pages = LaidbackPaginator(Entry.live.all(), blog.entry_per_page)
    return render_to_response('list_entries.html', { 
        'blog': blog,
        'page':pages.page(page_num),
        'category_list': Category.objects.filter(shown=True),
        })

def show_index(request, blog_slug=None):
    ''' renders index page'''
    return list_entries(request, blog_slug, 1)

def show_category(request, blog_slug=None, category_slug=None, page_num=1):
    ''' lists entries under category specified by category_slug '''
    blog = get_blog(blog_slug)
    category = get_object_or_404(Category, slug=category_slug)
    entries = Entry.live.filter( category=category )
    pages = LaidbackPaginator(entries, blog.entry_per_page)
    return render_to_response('category_view.html', { 
        'blog': blog,
        'category': category,
        'page': pages.page(page_num),
        'category_list': Category.objects.filter(shown=True),
        })

def show_entry(request, entry_slug, blog_slug=None):
    blog = get_blog(blog_slug)
    entry = get_object_or_404(Entry, slug=entry_slug)
    return render_to_response('entry_view.html', { 
        'blog': blog,
        'category_list': Category.objects.filter(shown=True),
        'entry': entry,
        })

