from rest_framework_simplejwt.tokens import Token
from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class User(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AdminToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token