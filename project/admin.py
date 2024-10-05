from django.contrib import admin
from .models import Projects,Team,Client,Task

admin.site.register(Projects)
admin.site.register(Team)
admin.site.register(Client)
admin.site.register(Task)