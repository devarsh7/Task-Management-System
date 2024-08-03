from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     theme = models.CharField(max_length=10, choices=(('light', 'Light Mode'), ('dark', 'Dark Mode')), default='light')
#
#     def __str__(self):
#         return self.user.username

    
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255, default='Untitled Task')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    due_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=255, default='No message')
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField(default='No content')
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
