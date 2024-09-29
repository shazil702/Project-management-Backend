from django.db import models
from django.contrib.auth import get_user_model
from project.models import Team

User = get_user_model()

class EmployeeProfile(models.Model):
    employee = models.ForeignKey(User, related_name='employee', limit_choices_to={'is_employee':True}, on_delete=models.CASCADE)
    joined_date = models.DateField()
    team = models.ForeignKey(Team, related_name='employee_team', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.employee.username} Profile'

class EmployeePersonalInfo(models.Model):
    profile = models.OneToOneField(EmployeeProfile, on_delete=models.CASCADE,)
    idNumber = models.CharField(max_length=100)
    pan = models.CharField(max_length=10)
    dob = models.DateField()
    genderChoices = [('male', 'Male'), ('female', 'Female')]
    gender = models.CharField(max_length=6, choices=genderChoices)
    bankAccountNumber = models.CharField(max_length=20)
    bankIFSC = models.CharField(max_length=11)
    bankBranch = models.CharField(max_length=155)
    salaryAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.profile} Personal Info'


