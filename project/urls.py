from django.urls import path
from . import views
urlpatterns = [
    path('viewAllProjects/', views.ProjectList.as_view(),name='project_list'),
    path('viewAllClients/',views.ClientListView.as_view(),name='client_view'),
]