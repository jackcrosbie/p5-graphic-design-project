""" django imports """
import uuid

from django.db import models
from django_countries.fields import CountryField

from profiles.models import Profile


project_choices = (
    ('custom', 'Custom'),
    ('website design', 'Website Design'),
    ('Maintenance', 'Maintenace'),
    ('Urgent Repair', 'Urgent Repair'),
)


class Quotes(models.Model):

    """ quote form categories and attributes """
    quote_id = models.CharField(max_length=32, default="", null=False, editable=False)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    project_type = models.CharField(max_length=20,
                                    choices=project_choices, default='custom')
    date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.CharField(max_length=20)
    message = models.TextField()

    def _generate_quote_id(self):
        """
        Generate a random, unique quote number using UUID
        """
        return uuid.uuid4().hex.upper()

    class Meta:
        """ change name for admin panel """
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.quote_id


class Order(models.Model):
    """ editbale=false is used for a unqiue order id which can't be changed"""
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, 
                                    null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
