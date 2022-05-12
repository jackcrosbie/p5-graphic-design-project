""" imports from django and views.py file """
from django.urls import path
from .views import ContactUsFormView


urlpatterns = [
    path('', ContactUsFormView.as_view(), name='contact'),
]
