""" imports from django and views.py"""
from django.urls import path
from .views import ReviewListView, ReviewDetailView, ReviewFormView, UpdateReviewView, DeleteReviewView

urlpatterns = [
    path('add_review/', ReviewFormView.as_view(), name='add_review'),
    path('', ReviewListView.as_view(), name='reviews'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(),
         name='reviews_detail'),
    path('review/update/<int:pk>', UpdateReviewView.as_view(), name='update_review'),
    path('review/<int:pk>/delete/', DeleteReviewView.as_view(), name='delete_review'),
]
