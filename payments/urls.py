""" imports from django and views.py"""
from django.urls import path
from . import views


urlpatterns = [
    path('payments/', views.payments, name='payments'),
    path('quotes/', views.payments, name='quotes'),
]