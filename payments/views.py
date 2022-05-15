""" import from django """
from django.shortcuts import render


# Create your views here.
def payments(request):
    """ Return homepage """
    return render(request, 'payments/payments.html')

def about(request):
    """ Return homepage """
    return render(request, 'payments/quotes.html')
