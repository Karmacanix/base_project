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

app_name = 'timesheets'
urlpatterns = [
    path('timelog/list/', views.TimeLogList.as_view(), name='timelog-list'),
    path('timelog/<int:pk>/', views.TimeLogDetail.as_view(), name='timelog-detail'),
    path('timelog/create/', views.TimeLogCreate.as_view(), name='timelog-create'),
    path('timelog/<int:pk>/update/', views.TimeLogUpdate.as_view(), name='timelog-update'),
]
