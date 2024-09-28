from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/',include('Authentication.urls')),
    path('hr/',include('Hr.urls')),
    path('project/',include('project.urls')),
    path('employee/',include('Employee.urls')),
]
