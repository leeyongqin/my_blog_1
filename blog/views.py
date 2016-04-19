#coding: utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.utils import timezone


def index(request):
    """

    Args:
        request:

    Returns:

    """
    if "date" in request.COOKIES:
        cookie_info = "The date is: %s" % request.COOKIES["date"]
        return render(request, 'index.html', {'title': '在不务正业的道路上策马奔腾', 'content': cookie_info,})
    else:
        cookie_info = "No date in cookies, we will set it in cookies"
        response = render_to_response('index.html', {'title': '在不务正业的道路上策马奔腾', 'content': cookie_info, })
        response.set_cookie('date', 'PP')
        return response


