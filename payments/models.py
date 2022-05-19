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
    quote_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    project_type = models.CharField(max_length=20,
                                    choices=project_choices, default='custom')
    date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        """ change name for admin panel """
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.name
