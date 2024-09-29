from rest_framework.generics import RetrieveUpdateAPIView
from .models import EmployeePersonalInfo, EmployeeProfile
from .serializers import EmployeeDetailsSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class EmployeeDetailsView(RetrieveUpdateAPIView):
    serializer_class = EmployeeDetailsSerializer

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(EmployeeProfile, employee=request.user)
        personalInfo = get_object_or_404(EmployeePersonalInfo, profile=profile)
        serializer = self.get_serializer({
            'profile': profile,
            'personal_info': personalInfo,
        })
        return Response(serializer.data)