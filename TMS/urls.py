from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.routers import DefaultRouter
from .api_endpoints import TaskViewSet
from .views import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, task_list, UserCreateView, \
    UserUpdateView, UserDeleteView, UserDetailView, CustomLoginView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.dashboard, name='dashboard'),
    path('accounts/register/', views.register, name='register'),
    path('bulk-task-action/', views.bulk_task_action, name='bulk-task-action'),
    path('tasks/bulk-action/', views.bulk_task_action, name='bulk_task_action'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('users/', views.users, name='users'),
    path('user/add/', UserCreateView.as_view(), name='user-add'),
    path('user/<int:pk>/edit/', UserUpdateView.as_view(), name='user-edit'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Other URL patterns
]
