from rest_framework import serializers
from .models import EmployeePersonalInfo, EmployeeProfile
from Authentication.serializers import UserSerializer

class EmployeeProfileSerializer(serializers.ModelSerializer):
    employee = UserSerializer(fields=['username', 'email', 'phone'])
    class Meta:
        model = EmployeeProfile
        fields = '__all__'

class EmployeePersonalInfoSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()
    class Meta:
        model = EmployeePersonalInfo
        fields = '__all__'

class EmployeeDetailsSerializer(serializers.Serializer):
    profile = EmployeeProfileSerializer()
    personal_info = EmployeePersonalInfoSerializer()
