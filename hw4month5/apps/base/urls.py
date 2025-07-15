from django.urls import path
from .views import (
    ProjectListCreateView, ProjectRetrieveUpdateDestroyView,
    TaskListCreateView, TaskRetrieveUpdateDestroyView,
    ProjectTaskListView
)

urlpatterns = [
    
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),

 
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),

  
    path('api/projects/<int:project_id>/tasks/', ProjectTaskListView.as_view(), name='project-task-list'),
]
