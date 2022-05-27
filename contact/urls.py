""" imports from django and views.py file """
from django.urls import path
from .views import ContactUsFormView, NewsletterFormView


urlpatterns = [
    path('', ContactUsFormView.as_view(), name='contact'),
    path('newsletter/', NewsletterFormView.as_view(), name='newsletter'),
]
