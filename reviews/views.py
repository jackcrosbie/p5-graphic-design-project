""" imports from django, models.py and forms.py """
from django.views.generic import ListView, DetailView
from .models import UserReviews
from .forms import UserReviewForm


class ReviewListView(ListView):
    """ view for generating the review list """
    model = UserReviews
    template_name = "reviews/reviews.html"
    form_class = UserReviewForm
    success_url = '/'


class ReviewDetailView(DetailView):
    """ view for generation Review Details """
    model = UserReviews
    template_name = "reviews/reviews_detail.html"

