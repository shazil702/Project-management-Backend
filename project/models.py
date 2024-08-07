from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model

class Projects(models.Model):
    statusChoices = [('notStarted', 'Not Started'), ('inProgress', 'In Progress'), ('completed', 'Completed')]
    projectName = models.CharField(max_length=300)
    description = models.TextField()
    startDate = models.DateField()
    teamLead = models.ForeignKey(User, related_name='projectLead', on_delete=models.DO_NOTHING, limit_choices_to={'is_tl':True})
    teamMemebers = models.ManyToManyField(User, related_name='projects', limit_choices_to={'is_employee': True})
    status = models.CharField(max_length=25, choices=statusChoices, default='notStarted')
    dueDate = models.DateField()
    
    def __str__(self):
        return self.projectName