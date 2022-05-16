""" imports from django and views.py"""
from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
]
