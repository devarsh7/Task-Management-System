from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255, default='Untitled Task')
    description = models.TextField(max_length=500, default='Add Description')  # Ensure this line is present
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    due_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE, default=1)
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


