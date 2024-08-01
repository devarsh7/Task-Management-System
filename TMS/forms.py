from django import forms
from .models import Task, Message

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'assigned_to', 'due_date']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
