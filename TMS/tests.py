from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Task
from .serializers import TaskSerializer


class TaskAPITestCase(APITestCase):
    # Method will initialize test data before each test method
    def setUp(self):
        self.user = User.objects.create_user(username='devarsh', password='admin123')
        self.task1 = Task.objects.create(title="Task 1", assigned_to=self.user)
        self.task2 = Task.objects.create(title="Task 2", assigned_to=self.user)
        self.valid_payload = {
            'title': 'New Task',
            'assigned_to': self.user.id
        }
        self.invalid_payload = {
            'title': '',
            'assigned_to': self.user.id
        }

    # Test case to check weather new task is created or not
    def test_create_task(self):
        url = reverse('task_list')
        response = self.client.post(url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    # Test case to check weather new task is created with invalid data
    def test_create_task_invalid(self):
        url = reverse('task_list')
        response = self.client.post(url, data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test case to fetch all the tasks
    def test_list_tasks(self):
        url = reverse('task_list')
        response = self.client.get(url, format='json')
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # Test case to check to fetch a given task with id
    def test_retrieve_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        response = self.client.get(url, format='json')
        serializer = TaskSerializer(self.task1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # Test case to update an existing task of that id
    def test_update_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        response = self.client.put(url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, self.valid_payload['title'])

    # Test case to delete any task of the given id
    def test_delete_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)
