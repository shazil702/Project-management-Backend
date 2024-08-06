from django.urls import path
from . import views
urlpatterns = [
    path('admintoken/', views.AdminTokenView.as_view(),name='admin_token'),
]