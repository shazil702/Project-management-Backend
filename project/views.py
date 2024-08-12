from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects
from .serializer import Project_Serializer

class ProjectList(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        serializer = Project_Serializer(projects, many=True)
        return Response(serializer.data)
