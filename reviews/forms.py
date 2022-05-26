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

    def form_valid(self, form):
        # if form is valid return to discussion
        form.instance.user = self.request.user
        return super().form_valid(form)