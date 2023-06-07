# flake8: noqa
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', status=201, context={
        'name': 'Eduardo',
    })

def contact(request):
    return HttpResponse("Contact")

def about(request):
    return HttpResponse("About")
