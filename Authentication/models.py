from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_tl = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)