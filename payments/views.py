""" imports from django, models.py and forms.py """
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.conf import settings
import stripe

import os

from .models import Quotes
from .forms import QuotesForm

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY', '')

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

    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken'],
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description="Deposit"
        )

    return HttpResponseRedirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'payments/payment_success.html', {'amount': amount})