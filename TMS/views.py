from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Task
from .forms import TaskForm
from django.contrib import messages


def is_admin(user):
    return user.is_staff

@login_required
def task_list(request):
    query = request.GET.get('q', '')
    if request.user.is_staff:
        if query:
            tasks = Task.objects.filter(Q(title__icontains=query))
        else:
            tasks = Task.objects.all()
    else:
        if query:
            tasks = Task.objects.filter(Q(title__icontains=query), Q(created_by=request.user) | Q(assigned_to=request.user))
        else:
            tasks = Task.objects.filter(Q(created_by=request.user) | Q(assigned_to=request.user))

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


class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('dashboard')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
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
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(Q(created_by=self.request.user) | Q(assigned_to=self.request.user))
        return qs

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(Q(created_by=self.request.user) | Q(assigned_to=self.request.user))
        return qs


@login_required
def dashboard(request):
    if request.user.is_staff:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(Q(created_by=request.user) | Q(assigned_to=request.user))

    completed_tasks_count = tasks.filter(status='Completed').count()
    pending_tasks_count = tasks.filter(status='Pending').count()
    users_count = User.objects.count()
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
        'overdue_tasks_count': overdue_tasks_count,
        'due_today_count': due_today_count,
        'my_tasks_count': my_tasks_count,
        'upcoming_deadlines': upcoming_deadlines,
    }
    return render(request, 'dashboard.html', context)

def users(request):
    users_list = User.objects.all()
    return render(request, 'users.html', {'users': users_list})

class UserCreateView(UserPassesTestMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users')

    def test_func(self):
        return self.request.user.is_staff

class UserUpdateView(UserPassesTestMixin,UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'user_form.html'
    success_url = reverse_lazy('users')

    def test_func(self):
        return self.request.user.is_staff

class UserDeleteView(UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('users')

    def test_func(self):
        return self.request.user.is_staff

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'
