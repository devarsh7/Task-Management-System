from django import forms
from .models import Task, User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'assigned_to', 'due_date', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
