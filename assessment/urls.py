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
from django.contrib import admin
from django.urls import include, path
from assessment import views

app_name = 'assessment'
urlpatterns = [
    path('application/create/', views.ApplicationCreate.as_view(), name='application-create'),
    path('application/list/', views.ApplicationList.as_view(), name='application-list'),
    path('application/<str:pk>/', views.ApplicationDetail.as_view(), name='application-detail'),
    path('application/<str:pk>/update/', views.ApplicationUpdate.as_view(), name='application-update'),
    path('application/<str:pk>/delete/', views.ApplicationDelete.as_view(), name='application-delete'),
    path('cloudquestionnaire/<str:pk>/', views.CloudQuestionnaireDetail.as_view(), name='cloudquestionnaire-detail'),
    path('cloudquestionnaire/<str:pk>/create/', views.CloudQuestionnaireCreate.as_view(), name='cloudquestionnaire-create'),
    path('cloudquestionnaire/<str:pk>/update/', views.CloudQuestionnaireUpdate.as_view(), name='cloudquestionnaire-update'),
    path('cloudquestionnaire/<str:pk>/delete/', views.CloudQuestionnaireDelete.as_view(), name='cloudquestionnaire-delete'),
    path('ictbriefcloudriskassessment/<str:pk>/', views.CloudICTBriefCloudRiskAssessmentDetail.as_view(), name='ictbriefcloudriskassessment-detail'),
    path('ictbriefcloudriskassessment/<str:pk>/create/', views.CloudICTBriefCloudRiskAssessmentCreate.as_view(), name='ictbriefcloudriskassessment-create'),
    path('ictbriefcloudriskassessment/<str:pk>/update/', views.CloudICTBriefCloudRiskAssessmentUpdate.as_view(), name='ictbriefcloudriskassessment-update'),
    path('ictbriefcloudriskassessment/<str:pk>/delete/', views.CloudICTBriefCloudRiskAssessmentDelete.as_view(), name='ictbriefcloudriskassessment-delete'),
    path('informationclassification/<str:pk>/', views.InformationClassificationDetail.as_view(), name='informationclassification-detail'),
    path('informationclassification/<str:pk>/create/', views.InformationClassificationCreate.as_view(), name='informationclassification-create'),
    path('informationclassification/<str:pk>/update/', views.InformationClassificationUpdate.as_view(), name='informationclassification-update'),
    path('informationclassification/<str:pk>/delete/', views.InformationClassificationDelete.as_view(), name='informationclassification-delete'),
    # path('privacyassessment/<int:pk>/', views.PrivacyAssessmentDetail.as_view(), name='privacyassessment-detail'),
    # path('privacyassessment/<int:pk>/create/', views.PrivacyAssessmentCreate.as_view(), name='privacyassessment-create'),
    # path('privacyassessment/<int:pk>/update/', views.PrivacyAssessmentUpdate.as_view(), name='privacyassessment-update'),
    # path('privacyassessment/<int:pk>/delete/', views.PrivacyAssessmentDelete.as_view(), name='privacyassessment-delete'),
]
