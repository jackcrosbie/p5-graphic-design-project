""" imports from django and views.py"""
from django.urls import path
from . import views
from .views import QuotesFormView


urlpatterns = [
    path('payments/', views.payments, name='payments'),
    path('quotes/', QuotesFormView.as_view(), name='quotes'),
]
