from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user}"
