""" imports from django, models.py and forms.py """
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.conf import settings
import stripe

import os

from .models import Quotes
from .forms import QuotesForm

stripe.api_key = "sk_test_51Kdc2gEQtc7mNL2U0oEWtxrMRkHHxEmI5qC3K3ZnhiZw6EKatXTPIhREahO2hcwz1HBbW1lBgYLjXqeu7mClVImQ000gnUdZsy"

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

    return HttpResponseRedirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'payments/payment_success.html', {'amount': amount})