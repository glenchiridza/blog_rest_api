from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="writ_profile/", max_length=255, blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}"


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="sub_profile/", max_length=255, blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}"
