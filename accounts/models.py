from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
