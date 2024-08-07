from django.urls import path
from . import views
urlpatterns = [
    path('viewEmployee/', views.EmployeeList.as_view(),name='employee_list'),
]