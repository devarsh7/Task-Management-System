from .models import Task, Message, User
from django import forms
#from .models import Profile

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
# class ThemeForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['theme']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'assigned_to', 'due_date']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
