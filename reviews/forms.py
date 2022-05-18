""" django and model imports """
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """ meta data to generate contact us form """
    class Meta:
        """ form model, fields and widgets used"""
        model = Review
        fields = [
            'user', 'comment', 'rate'
            ]
