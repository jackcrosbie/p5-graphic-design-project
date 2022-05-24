""" django imports """
from django.db import models
import uuid


project_choices = (
    ('custom', 'Custom'),
    ('website design', 'Website Design'),
    ('Maintenance', 'Maintenace'),
    ('Urgent Repair', 'Urgent Repair'),
)


class Quotes(models.Model):

    """ quote form categories and attributes """
    quote_id = models.CharField(max_length=32, null=False, editable=False)
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
