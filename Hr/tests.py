import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from Authentication.serializers import UserSerializer

@pytest.mark.django_db
def test_employee_list():
    client = APIClient()
    User = get_user_model()
    employee1 = User.objects.create_user(email='employee1@gmail.com', username='employee1', password='opu2342', phone='432432',is_employee=True)
    employee2 = User.objects.create_user(email='employee2@gmail.com', username='employee2', password='hlk45434', phone='53234', is_employee=True)
    not_employee = User.objects.create_user(email='notemployee@gmail.com', username='notemployee', password='ur53532', phone='345323', is_employee=False)

    url = reverse('employee_list')
    response = client.get(url)
    data = UserSerializer([employee1, employee2], many=True).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data