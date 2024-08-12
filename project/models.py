from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Team(models.Model):
    teamName = models.CharField(max_length=255)
    tl = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='teamLead', limit_choices_to={'is_tl':True})
    teamMembers = models.ManyToManyField(User, related_name='teamMember',limit_choices_to={'is_employee':True})

    def __str__(self):
        return self.teamName
    
class Projects(models.Model):
    statusChoices = [('notStarted', 'Not Started'), ('inProgress', 'In Progress'), ('completed', 'Completed')]
    projectName = models.CharField(max_length=300)
    description = models.TextField()
    startDate = models.DateField()
    status = models.CharField(max_length=25, choices=statusChoices, default='notStarted')
    dueDate = models.DateField()
    team = models.ForeignKey(Team, related_name='team', on_delete=models.DO_NOTHING, null=True, blank=True)
    
    def __str__(self):
        return self.projectName
    