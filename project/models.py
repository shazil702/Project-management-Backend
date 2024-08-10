from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Projects(models.Model):
    statusChoices = [('notStarted', 'Not Started'), ('inProgress', 'In Progress'), ('completed', 'Completed')]
    projectName = models.CharField(max_length=300)
    description = models.TextField()
    startDate = models.DateField()
    status = models.CharField(max_length=25, choices=statusChoices, default='notStarted')
    dueDate = models.DateField()
    
    def __str__(self):
        return self.projectName
    
class Team(models.Model):
    teamName = models.CharField(max_length=255)
    tl = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='teamLead')
    teamMembers = models.ManyToManyField(User, related_name='teamMember')

    def __str__(self):
        return self.teamName