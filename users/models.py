from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    blocked_until = models.DateTimeField(default=None, null=True)
    is_admin = models.BooleanField(default=False)
