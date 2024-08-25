from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .serializers import AdminToken
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.mail import send_mail
from ProjectManagement import settings
from django.shortcuts import get_object_or_404
import random
from datetime import timedelta

class AdminTokenView(TokenObtainPairView):
    serializer_class = AdminToken
    def post(self, request, *args, **kwargs):
        user = User.objects.get(email = request.data['email'])
        print(user.email)
        print(user.is_superuser)
        if not user.is_superuser:
            return Response({"message":"user is not super user"}, status=status.HTTP_403_FORBIDDEN)
        response = super().post(request, *args, **kwargs)
        return response
    def get_serializer_context(self):
        return super().get_serializer_context()

class SendOTP(APIView):
    def post(self, request):
        mail = request.data['email']
        user = get_object_or_404(User,email=mail)
        otp = str(random.randint(100000, 999999))
        subject = 'Login OTP'
        message = f'Your one time password for Login is {otp}'
        from_mail = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_mail, [mail])
        token = AccessToken.for_user(user)
        token.set_exp(lifetime=timedelta(minutes=2))
        token['otp'] = otp
        token['email'] = mail
        return Response({'otp_token': str(token),}, status=status.HTTP_200_OK)

class VerifyOTP(APIView):
    def post(self, request):
        otpToken = request.data.get('otp_token')
        userOTP = request.data.get('otp')
        try:
            token = AccessToken(otpToken)
            otp = token['otp']
            email = token['email']
            if otp == userOTP:
                user = get_object_or_404(User,email=email)
                refreshToken = RefreshToken.for_user(user)
                return Response({'refresh_token': str(refreshToken), 'access_token': str(refreshToken.access_token)}, status=status.HTTP_200_OK)
            else:
                 return Response({"message": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
             return Response({"message": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)