from django.urls import path
from . import views
urlpatterns = [
    path('profile/', views.EmployeeDetailsView.as_view(),name='employee_list'),
]