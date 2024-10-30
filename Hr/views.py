from rest_framework.response import Response
from rest_framework.views import APIView
from Authentication.models import User
from Authentication.serializers import UserSerializer
from rest_framework import status

class EmployeeList(APIView):
    def get(self, request):
        employees = User.objects.exclude(username=request.user.username)
        serializer = UserSerializer(employees, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
