from .models import Projects, Client
from rest_framework import serializers

class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
