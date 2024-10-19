from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'is_superuser', 'is_hr', 'is_tl', 'is_employee', 'phone', 'img']
    
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields',None)
        super(UserSerializer, self).__init__(*args, **kwargs)
        if fields:
            allowed = set(fields)
            exsisting = set(self.fields)
            for field_name in exsisting - allowed:
                self.fields.pop(field_name)

class AdminToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
        