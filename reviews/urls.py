""" imports from django and views.py"""
from django.urls import path
from .views import ReviewListView

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews'),
]
