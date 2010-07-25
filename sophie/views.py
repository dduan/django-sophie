from django.template import RequestContext
from django.template.loader import select_template
from django.shortcuts import  get_object_or_404, render_to_response
from django.utils.functional import curry

from sophie.models import Blog, Category, Entry
from sophie.utils import LaidbackPaginator, multiblog_enabled, route_template


def list_entries( request, blog_slug=None, page_num=1 ):
    ''' renders requested page, a list of date-ordred entries '''
    blog = Blog.get_blog(blog_slug)
    pages = LaidbackPaginator(blog.get_entries(), blog.page_length)

    # curry it up to save typing!
    route = curry(route_template, blog_slug=blog.slug)

    context = RequestContext(request, { 
        'blog': blog,
        'page': pages.page(page_num),
        'multiblog': multiblog_enabled,
    })
    # sidebar here is rendered manually because {% include %} does not
    # accept a compiled template as an argument.
    context['sidebar'] = select_template( route('sidebar') ).render(context)
    context['base_template'] = select_template( route('base') )
    return render_to_response( route('entry_list'), {}, context )

def show_index(request, blog_slug=None):
    ''' renders index page'''
    return list_entries(request, blog_slug)

def show_category(request, blog_slug=None, category_slug=None, page_num=1):
    ''' lists entries under category specified by category_slug '''
    blog = Blog.get_blog(blog_slug)
    category = get_object_or_404(Category, blog=blog, slug=category_slug)
    entries = Entry.live.filter( category=category )
    pages = LaidbackPaginator(entries, blog.page_length)
    route = curry(route_template,extraname=category.slug,blog_slug=blog.slug)
    context = RequestContext(request, {
        'blog': blog,
        'category': category,
        'page': pages.page(page_num),
        'multiblog': multiblog_enabled,
    }) 
    # sidebar here is rendered manually because {% include %} does not
    # accept a compiled template as an argument.
    context['sidebar'] = select_template( route('sidebar') ).render(context)
    context['base_template'] = select_template( route('base') )
    return render_to_response( route('category_details'), {}, context )

def show_entry(request, entry_slug, blog_slug=None):
    blog = Blog.get_blog(blog_slug)
    entry = get_object_or_404(Entry, slug=entry_slug)
    route = curry(route_template, extraname=entry.slug, blog_slug=blog.slug)
    context = RequestContext(request, {
        'blog': blog,
        'entry': entry,
        'multiblog': multiblog_enabled,
    })
    # sidebar here is rendered manually because {% include %} does not
    # accept a compiled template as an argument.
    context['sidebar'] = select_template( route('sidebar') ).render(context)
    context['base_template'] = select_template( route('base') )
    return render_to_response( route('entry_details'), {}, context )
