""" imports from django and views.py"""
from django.urls import path
from .views import ReviewFormView

urlpatterns = [
    path('', ReviewFormView.as_view(), name='reviews'),
]
