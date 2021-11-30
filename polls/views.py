from django.shortcuts import render

from django.http import HttpResponse

from .open_library import get_by_isbn

def index(request):
    return HttpResponse("Hello, world. " + get_by_isbn('a'))
