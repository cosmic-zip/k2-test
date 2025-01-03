from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from fakeapi.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

class HealthyViewTest(APITestCase):

    def test_healthy_view(self):
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "ok", "message": "API is healthy"})


class UserViewTest(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="user", password="password", role="user")
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    def test_user_view(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get('/user/', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)
        self.assertEqual(response.data["role"], self.user.role)

class AdminViewTest(APITestCase):

    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(
            username="admin",
            password="password",
            role="admin",
            is_staff=True,
            is_superuser=True
        )
        refresh = RefreshToken.for_user(self.admin_user)
        self.token = str(refresh.access_token)

    def test_admin_view(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get('/admin/', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.admin_user.username)
        self.assertEqual(response.data["role"], self.admin_user.role)
