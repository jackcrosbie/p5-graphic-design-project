""" import from django """
from django.shortcuts import render


# Create your views here.
def index(request):
    """ Return homepage """
    return render(request, 'home/index.html')

def about(request):
    """ Return homepage """
    return render(request, 'home/about.html')

def pricing(request):
    """ Return homepage """
    return render(request, 'home/pricing.html')
