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
    path('select/', views.timesheet_select, name='timesheet-select'),
    path('<timesheet_name>/', views.TimesheetLines.as_view(), name='timesheet-lines'),
    path('<timesheet_name>/create/', views.TimesheetLineCreate.as_view(), name='timesheet-line-create'),
    path('<timesheet_name>/edit/<int:pk>/', views.TimesheetLineEdit.as_view(), name='timesheet-line-edit'),
]
