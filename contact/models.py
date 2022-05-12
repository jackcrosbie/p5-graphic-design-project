from django.db import models


class ContactUs(models.Model):

    """ contact form categories and attributes """
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    date = models.DateField()
    message = models.TextField()
