# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('notifications/<int:pk>/mark-as-read/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('projects/', views.projects, name='projects'),
    path('users/', views.users, name='users'),
    path('reports/', views.reports, name='reports'),
    # Other URL patterns
]
