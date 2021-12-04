from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # avatar = models.ImageField(null=True, blank=True, upload_to='avatars/')
    phone = models.CharField(max_length=255, default='none')
    address = models.CharField(max_length=255, default='none')


