from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ A view to return the index page """
    return render(request, 'landing/index.html')
