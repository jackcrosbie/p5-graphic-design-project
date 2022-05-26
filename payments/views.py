""" imports from django, models.py and forms.py """
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Quotes
from .forms import QuotesForm


# Create your views here.
class QuotesFormView(CreateView):
    """ view for generating the contact form """
    model = Quotes()
    template_name = "payments/quotes.html"
    form_class = QuotesForm
    success_url = '/'


def payments(request):
    """ Return homepage """
    return render(request, 'payments/payments.html')


def about(request):
    """ Return homepage """
    return render(request, 'payments/quotes.html')


def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)

        return redirect (reverse('success', args=[amount]))


def successMessage(request, args):
    amount = args
    return render(request, 'payments/payment_success.html', {'amount': amount})