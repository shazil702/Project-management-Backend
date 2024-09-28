from rest_framework import serializers
from .models import EmployeePersonalInfo, EmployeeProfile

class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = '__all__'

class EmployeePersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePersonalInfo
        fields = '__all__'

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    profile = EmployeeProfileSerializer()
    personal_info = EmployeePersonalInfoSerializer()
