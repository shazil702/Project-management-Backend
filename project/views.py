from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Client, Task
from .serializer import Project_Serializer, Client_Serializer, Task_Serializer
from rest_framework import status, generics

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

class TaskDetailView(APIView):
    def get(self, request, project_id):
        try:
            project = Projects.objects.get(id=project_id)
            tasks = Task.objects.filter(project=project, user=request.user)
            serializer = Task_Serializer(tasks, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserProjectView(generics.ListAPIView):
    serializer_class = Project_Serializer

    def get_queryset(self):
        user = self.request.user
        return Projects.objects.filter(team__teamMembers=user)
    
    def get_serializer(self, *args, **kwargs):
        kwargs['fields'] = ['id', 'projectName', 'status', 'startDate', 'dueDate', 'client']
        return super(UserProjectView, self).get_serializer(*args, **kwargs)