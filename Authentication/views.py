from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import AdminToken
from .models import User
from rest_framework.response import Response
from rest_framework import status


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