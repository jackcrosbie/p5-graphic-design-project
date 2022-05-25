""" django and model imports """
from django import forms
from .models import UserReviews

class ReviewForm(forms.ModelForm):
    """ meta data to generate contact us form """
    class Meta:
        """ form model, fields and widgets used"""
        model = UserReviews
        fields = [
            'title', 'user', 'review', 'rate'
            ]
