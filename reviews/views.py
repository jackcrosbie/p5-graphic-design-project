""" imports from django, models.py and forms.py """
from django.shortcuts import render
from .models import Review
from django.views.generic.edit import CreateView
from .forms import ReviewForm


class ReviewFormView(CreateView):
    """ view for generating the contact form """
    model = Review()
    template_name = "reviews/reviews.html"
    form_class = ReviewForm
    success_url = '/'