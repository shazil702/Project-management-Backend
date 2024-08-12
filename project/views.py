from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Client
from .serializer import Project_Serializer, Client_Serializer

class ProjectList(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        serializer = Project_Serializer(projects, many=True)
        return Response(serializer.data)

class ClientListView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = Client_Serializer(clients, many=True)
        return Response(serializer.data)
