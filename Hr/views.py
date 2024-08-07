from rest_framework.response import Response
from rest_framework.views import APIView
from Authentication.models import User
from Authentication.serializers import UserSerializer
from rest_framework import status

class EmployeeList(APIView):
    def get(self, request):
        employees = User.objects.filter(is_employee = True)
        serializer = UserSerializer(employees, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
