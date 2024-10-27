from .models import Projects, Client, Task, Team
from rest_framework import serializers
from Authentication.serializers import UserSerializer

class Team_Serializer(serializers.ModelSerializer):
    tl = UserSerializer()
    teamMembers = UserSerializer(many=True)
    class Meta:
        model = Team
        fields = '__all__'

class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class Task_Serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = '__all__'

class Project_Serializer(serializers.ModelSerializer):
    client = Client_Serializer()
    team = Team_Serializer()
    tasks = Task_Serializer(many=True)
    class Meta:
        model = Projects
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields',None)
        super(Project_Serializer, self).__init__(*args, **kwargs)
        if fields:
            allowed = set(fields)
            exsisting = set(self.fields)
            for field_name in exsisting - allowed:
                self.fields.pop(field_name)

