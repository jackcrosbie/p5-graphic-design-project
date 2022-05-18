from django.shortcuts import render
from .models import Review
from django.views.generic.edit import CreateView


def reviews(request):
    """ Return homepage """
    return render(request, 'reviews/reviews.html')


class ReviewView(CreateView):
    """ view for generating the contact form """
    model = Review()
    template_name = "reviews/reviews.html"
    success_url = '/'