from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Model representing a task in the task management system
class Task(models.Model):
    # Choices for the status of the task
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    # Title of the task, with a maximum length of 255 characters
    title = models.CharField(max_length=255, default='Untitled Task')

    # Description of the task, with a maximum length of 500 characters
    description = models.TextField(max_length=500, default='Add Description')  # Ensure this line is present

    # Status of the task, restricted to one of the STATUS_CHOICES
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    # Due date for the task, defaults to the current date
    due_date = models.DateField(default=timezone.now)

    # Timestamp for when the task was created, defaults to the current time
    created_at = models.DateTimeField(default=timezone.now)

    # Timestamp for when the task was last updated, defaults to the current time
    updated_at = models.DateTimeField(auto_now=True)

    # Reference to the user who created the task, with a default user ID of 1
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE, default=1)

    # Reference to the user to whom the task is assigned
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)

    # String representation of the task, which will be the title of the task
    def __str__(self):
        return self.title
