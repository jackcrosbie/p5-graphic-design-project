from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """ meta data to generate contact us form """
    class Meta:
        """ form model, fields and widgets used"""
        model = ContactUs
        fields = [
            'name', 'phone_number', 'email', 'date', 'message'
            ]
