"""iam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('project/list/', views.ProjectList.as_view(), name='project-list'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('project/create/', views.ProjectCreate.as_view(), name='project-create'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
    path('project/approvers/create/', views.ProjectApproversCreate.as_view(), name='project-approvers-create'),
    path('project/<int:pk>/approvers/update/', views.ProjectApproversUpdate.as_view(), name='project-approvers-update'),
    path('project/<int:project>/task/list/', views.TaskList.as_view(), name='task-list'),
    path('project/<int:project_id>/team/list/', views.TeamList.as_view(), name='team-list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
    path('team/<int:pk>/', views.TeamDetail.as_view(), name='team-detail'),
    path('team/<int:project_id>/create/', views.TeamCreate.as_view(), name='team-create'),
    path('team/<int:project_id>/update/<int:pk>/', views.TeamUpdate.as_view(), name='team-update'),
]
