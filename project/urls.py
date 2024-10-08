from django.urls import path
from . import views
urlpatterns = [
    path('viewAllProjects/', views.ProjectList.as_view(),name='project_list'),
    path('projectDetail/<int:project_id>/', views.ProjectList.as_view(), name='project_detail'),
    path('viewAllClients/',views.ClientListView.as_view(),name='client_view'),
    path('taskDetails/<int:project_id>/', views.TaskDetailView.as_view(),name='task_details'),
    path('userProjects/', views.UserProjectView.as_view(),name='user_project_view'),
]