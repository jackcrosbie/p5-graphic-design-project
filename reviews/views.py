""" imports from django, models.py and forms.py """
from .models import UserReviews
from .forms import ReviewForm
from django.views.generic import ListView


class ReviewListView(ListView):
    """ view for generating the contact form """
    model = UserReviews()
    template_name = "reviews/reviews.html"
    form_class = ReviewForm
    success_url = '/'

