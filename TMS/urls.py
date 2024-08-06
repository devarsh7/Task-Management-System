from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.routers import DefaultRouter
from .api_endpoints import TaskViewSet
from .views import (
    TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView,
    task_list, UserCreateView, UserUpdateView, UserDeleteView,
    UserDetailView, CustomLoginView
)

# Setting up the router for the API endpoints
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# URL patterns for the application
urlpatterns = [
    # Include the API URLs
    path('api/', include(router.urls)),

    # Dashboard view
    path('', views.dashboard, name='dashboard'),

    # User registration view
    path('accounts/register/', views.register, name='register'),

    # Bulk task action view
    path('bulk-task-action/', views.bulk_task_action, name='bulk-task-action'),

    # Task list and bulk action views
    path('tasks/bulk-action/', views.bulk_task_action, name='bulk_task_action'),
    path('tasks/', task_list, name='task_list'),

    # Task CRUD views
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # User list and CRUD views
    path('users/', views.users, name='users'),
    path('user/add/', UserCreateView.as_view(), name='user-add'),
    path('user/<int:pk>/edit/', UserUpdateView.as_view(), name='user-edit'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Authentication views for login and logout
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Other URL patterns can be added here
]
