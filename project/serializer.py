from .models import Projects, Client, Task
from rest_framework import serializers

class Project_Serializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
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


class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'