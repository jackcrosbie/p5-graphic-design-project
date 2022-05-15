from django.db import models


class Quotes(models.Model):

    """ quote form categories and attributes """
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
