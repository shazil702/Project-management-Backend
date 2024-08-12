from .models import Projects
from rest_framework import serializers

class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
