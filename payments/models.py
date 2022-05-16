from django.db import models


project_choices = (
    ('custom', 'Custom'),
    ('website design', 'Website Design',)
)


class Quotes(models.Model):

    """ quote form categories and attributes """
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    project_type = models.CharField(max_length=20, choices=project_choices, default='custom')
    date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.CharField(max_length=20)
    message = models.TextField()
