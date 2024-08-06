import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status

@pytest.mark.django_db
def test_admin_token():
    client = APIClient()
    User = get_user_model()
    superuser = User.objects.create_superuser(email='superuser@example.com', password='password123',username='superuser',phone='345678')
    user = User.objects.create_user(email='user@example.com', password='password123',username='user',phone='293743')
    response =client.post(reverse('admin_token'), {'email': 'superuser@example.com', 'password': 'password123'})
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data

    response = client.post(reverse('admin_token'), {'email': 'user@example.com', 'password': 'password123'})
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data['message'] == 'user is not super user'