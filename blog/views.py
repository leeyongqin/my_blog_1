# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from blog.models import Blog
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

"""
def index(request):

    if "date" in request.COOKIES:
        cookie_info = "The date is: %s" % request.COOKIES["date"]
        return render(request, 'index.html', {'title': '在不务正业的道路上策马奔腾', 'content': cookie_info, })
    else:
        cookie_info = "No date in cookies, we will set it in cookies"
        response = render_to_response('index.html', {'title': '在不务正业的道路上策马奔腾', 'content': cookie_info, })
        response.set_cookie('date', 'PP')
        return response
"""

def index(request):
    blogs = Blog.objects.all()
    index_paginator = Paginator(blogs, 4)
    page = request.GET.get('page')
    if page:
        current_page = int(page)
        if current_page > index_paginator.num_pages:
            current_page = index_paginator.num_pages
    else:
        current_page = 1

    previous_page = current_page - 1
    next_page = current_page + 1

    """
    try:
        blogs = Paginator.page(page_num)
    """
    try:
        blogs = index_paginator.page(page)
    except PageNotAnInteger:
        blogs = index_paginator.page(1)
    except EmptyPage:
        blogs = index_paginator.page(index_paginator.num_pages)

    context = {'title': '在不务正业的道路上策马奔腾',
               'blogs': blogs,
               'paginator': index_paginator.num_pages,
               'last_page': previous_page,
               'current_page': current_page,
               'next_page': next_page,
               'total_page': index_paginator.num_pages,
               }
    return render(request, 'index.html', context)