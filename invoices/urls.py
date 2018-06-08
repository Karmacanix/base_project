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

app_name = 'invoices'
urlpatterns = [
	path('customer/list/', views.CustomerList.as_view(), name='customer-list'),
    path('customer/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    path('customer/create/', views.CustomerCreate.as_view(), name='customer-create'),
    path('customer/<int:pk>/update/', views.CustomerUpdate.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete/', views.CustomerDelete.as_view(), name='customer-delete'),
    path('invoice/<str:week>/<str:project>/<str:settings>/', views.Invoice.as_view(), name='invoice'),
    path('params/', views.InvoiceParams.as_view(), name='invoice-params'),
    path('settings/list/', views.InvoiceSettingsList.as_view(), name='settings-list'),
    path('settings/<int:pk>/', views.InvoiceSettingsDetail.as_view(), name='settings-detail'),
    path('settings/create/', views.InvoiceSettingsCreate.as_view(), name='settings-create'),
    path('settings/<int:pk>/update/', views.InvoiceSettingsUpdate.as_view(), name='settings-update'),
    path('settings/<int:pk>/delete/', views.InvoiceSettingsDelete.as_view(), name='settings-delete'),
]
