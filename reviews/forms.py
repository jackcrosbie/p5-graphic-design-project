""" django and model imports """
from django import forms
from .models import UserReviews


class UserReviewForm(forms.ModelForm):
    """ meta data to generate contact us form """
    class Meta:
        """ form model, fields and widgets used"""
        model = UserReviews
        fields = [
            'title', 'review', 'rate'
            ]
