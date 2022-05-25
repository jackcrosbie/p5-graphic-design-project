""" imports from django, models.py and forms.py """
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import UserReviews
from .forms import UserReviewForm


class ReviewListView(ListView):
    """ view for generating the review list """
    model = UserReviews
    template_name = "reviews/reviews.html"
    ordering = ['-created_at']


class ReviewDetailView(DetailView):
    """ view for generation Review Details """
    model = UserReviews
    template_name = "reviews/reviews_detail.html"


class ReviewFormView(CreateView):
    """ view for review form """
    model = UserReviews
    template_name = "reviews/add_review.html"
    form_class = UserReviewForm
    success_url = reverse_lazy('reviews')


class UpdateReviewView(UpdateView):
    """ view for updating review form """
    model = UserReviews
    template_name = "reviews/update_review.html"
    form_class = UserReviewForm


class DeleteReviewView(DeleteView):
    """ view for deleting review form """
    model = UserReviews
    template_name = "reviews/delete_review.html"
    success_url = reverse_lazy('reviews')