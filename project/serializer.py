from .models import Projects, Client, Task
from rest_framework import serializers

class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'