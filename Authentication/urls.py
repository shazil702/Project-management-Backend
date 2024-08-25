from django.urls import path
from . import views
urlpatterns = [
    path('admintoken/', views.AdminTokenView.as_view(),name='admin_token'),
    path('sendOTP/',views.SendOTP.as_view()),
    path('verifyOTP/',views.VerifyOTP.as_view()),
]