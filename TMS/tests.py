"""
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Task
from django.contrib.auth.models import User

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_url = reverse('task_list')  # Make sure 'task-list' matches the name in your URL conf
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.user.id = 6

    def test_create_task(self):
        data = {
            "title": "Test Task",
            "assigned_to": self.user.id  # Use the id of the created user
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Ensure you have a URL pattern for the TaskViewSet in your urls.py file like so:
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .api_views import TaskViewSet

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet, basename='task')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
"""