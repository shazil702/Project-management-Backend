from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class HrProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_hr':True})
    joined_date = models.DateField()
    address = models.TextField()
    img = models.ImageField(null=True, blank=True)
    about = models.TextField()

    @property
    def name(self):
        return self.user.username
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def phone(self):
        return self.user.phone
    
    def __str__(self):
        return f"{self.user.username}'s HR Profile"