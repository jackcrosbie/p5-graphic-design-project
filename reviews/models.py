from django.db import models
from django.contrib.auth.models import User


RATINGS = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    comment = models.TextField(max_length=1000)
    rate = models.IntegerField(choices=RATINGS, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username