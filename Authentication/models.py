from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_tl = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    img = models.ImageField(null=True, blank=True, unique=True, upload_to='images')
    groups = models.ManyToManyField(Group, related_name='custom_users_group', blank=True, related_query_name='user')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True, related_query_name='user_permission')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username