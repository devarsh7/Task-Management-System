# tests.py
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer

class TaskAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.task1 = Task.objects.create(title='Task 1', status='Pending', assigned_to=self.user)
        self.task2 = Task.objects.create(title='Task 2', status='Completed', assigned_to=self.user)

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'New Task', 'status': 'Pending', 'assigned_to': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.get(id=3).title, 'New Task')

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.get(url, format='json')
        task = Task.objects.get(id=self.task1.id)
        serializer = TaskSerializer(task)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        data = {'title': 'Updated Task', 'status': 'Completed', 'assigned_to': self.user.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')
        self.assertEqual(self.task1.status, 'Completed')

    def test_partial_update_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        data = {'status': 'Completed'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.status, 'Completed')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)
"""