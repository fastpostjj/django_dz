from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def products_views(request):

    if request.method == 'POST':
        return HttpRequest('POST')
    else:
        return HttpRequest('non-POST')