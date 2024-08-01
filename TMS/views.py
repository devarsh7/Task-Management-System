# views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task, Notification, Message
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    tasks = Task.objects.all()
    completed_tasks_count = tasks.filter(status='Completed').count()
    pending_tasks_count = tasks.filter(status='Pending').count()
    users_count = User.objects.count()
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    messages = Message.objects.filter(receiver=request.user, is_read=False)

    context = {
        'tasks': tasks,
        'completed_tasks_count': completed_tasks_count,
        'pending_tasks_count': pending_tasks_count,
        'users_count': users_count,
        'notifications': notifications,
        'messages': messages,
    }
    return render(request, 'dashboard.html', context)
def mark_notification_as_read(request, pk):
    notification = Notification.objects.get(pk=pk)
    notification.is_read = True
    notification.save()
    return redirect('dashboard')

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

def projects(request):
    # Add any context you need to pass to the template
    context = {}
    return render(request, 'projects.html', context)

def users(request):
    # Add any context you need for the users page
    context = {}
    return render(request, 'users.html', context)

def reports(request):
    # Add any context you need for the reports page
    context = {}
    return render(request, 'reports.html', context)