from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Task, Notification, Message
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth import login as auth_login

def task_list(request):
    query = request.GET.get('q', '')
    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else:
        tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def bulk_task_action(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        task_ids = request.POST.getlist('task_ids')

        if action == 'complete':
            Task.objects.filter(id__in=task_ids).update(status='Completed')
        elif action == 'delete':
            Task.objects.filter(id__in=task_ids).delete()

        # Redirect to the referring page
        referer = request.META.get('HTTP_REFERER', 'dashboard')  # default to 'dashboard'
        return redirect(referer)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('tasks')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasks')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasks')
@login_required
def dashboard(request):
    tasks = Task.objects.all()
    completed_tasks_count = tasks.filter(status='Completed').count()
    pending_tasks_count = tasks.filter(status='Pending').count()
    users_count = User.objects.count()
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    messages = Message.objects.filter(receiver=request.user, is_read=False)

    now = timezone.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)

    overdue_tasks_count = tasks.filter(due_date__lt=start_of_day, status='Pending').count()
    due_today_count = tasks.filter(due_date__gte=start_of_day, due_date__lt=end_of_day, status='Pending').count()
    my_tasks_count = tasks.filter(assigned_to=request.user).count()
    upcoming_deadlines = tasks.filter(due_date__gte=now).order_by('due_date')[:5]

    context = {
        'tasks': tasks,
        'completed_tasks_count': completed_tasks_count,
        'pending_tasks_count': pending_tasks_count,
        'users_count': users_count,
        'notifications': notifications,
        'messages': messages,
        'overdue_tasks_count': overdue_tasks_count,
        'due_today_count': due_today_count,
        'my_tasks_count': my_tasks_count,
        'upcoming_deadlines': upcoming_deadlines,
    }
    return render(request, 'dashboard.html', context)
@login_required
def mark_notification_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    notification.is_read = True
    notification.save()
    return redirect('dashboard')

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

def projects(request):
    context = {}
    return render(request, 'projects.html', context)

def users(request):
    users_list = User.objects.all()
    return render(request, 'users.html', {'users': users_list})

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users')

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'user_form.html'
    success_url = reverse_lazy('users')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('users')

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

