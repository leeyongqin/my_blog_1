#coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
import time


def index(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, 'index.html', {'title': '我想和自己谈谈'})
