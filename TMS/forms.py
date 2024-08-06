from .models import Task, User
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'assigned_to', 'due_date']

