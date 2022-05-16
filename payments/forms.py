from django import forms
from .models import Quotes


class QuotesForm(forms.ModelForm):
    """ meta data to generate quotes form """
    class Meta:
        """ form models and fields used"""
        model = Quotes
        fields = [
            'name', 'phone_number', 'email', 'project_type', 'deadline_date', 'message',
            ]
