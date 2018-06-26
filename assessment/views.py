# django
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

# this app
from .models import Application, InformationClassification, CloudQuestionnaire #, PrivacyAssessment, NonFunctionals
from .forms import ApplicationForm, InformationClassificationForm, CloudQuestionnaireForm #, PrivacyAssessmentForm, NonFunctionalsForm

# Create your views here.
class ApplicationList(ListView):
    model = Application


class ApplicationDetail(DetailView):
    model = Application
        

    # def information_classification_exists(self, **kwargs):
    #     try:
    #         info_class=InformationClassification.objects.get(id=self.kwargs['pk'])
    #         return True
    #     except ObjectDoesNotExist:
    #         return False

    # def privacy_assessment_exists(self, **kwargs):
    #     try:
    #         info_class=PrivacyAssessment.objects.get(id=self.kwargs['pk'])
    #         return True
    #     except ObjectDoesNotExist:
    #         return False

    # def non_functional_assessment_exists(self, **kwargs):
    #     try:
    #         info_class=NonFunctionals.objects.get(id=self.kwargs['pk'])
    #         return True
    #     except ObjectDoesNotExist:
    #         return False

    def get_context_data(self, **kwargs):
        context = super(ApplicationDetail, self).get_context_data(**kwargs)
        a = Application.objects.get(pk=self.kwargs['pk'])
        if hasattr(a, 'informationclassification'):
            context['ic'] = True
        else:
            context['ic'] = False

        if hasattr(a, 'cloudquestionnaire'):
            context['cl'] = True
        else:
            context['cl'] = False
        # context['pa'] = ApplicationDetail.privacy_assessment_exists(self)
        # context['nf'] = ApplicationDetail.non_functional_assessment_exists(self)
        return context


class ApplicationCreate(SuccessMessageMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    success_message = 'Application successfully registered!'
    success_url = reverse_lazy('assessment:application-list')

    def get_initial(self):
        initial = super(ApplicationCreate, self).get_initial()
        initial['requestor'] = self.request.user
        return initial


class ApplicationUpdate(SuccessMessageMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    success_message = 'Application details successfully updated!'


class ApplicationDelete(SuccessMessageMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('assessment:application-list')
    success_message = "Application deleted!"


class InformationClassificationDetail(DetailView):
    model = InformationClassification


class InformationClassificationCreate(SuccessMessageMixin, CreateView):
    model = InformationClassification
    form_class = InformationClassificationForm
    success_message = 'Information Classification successfully saved!'
    success_url = reverse_lazy('assessment:application-list')

    # def post(self, request, *args, **kwargs):
    #     app = Application.objects.get(id=self.kwargs['pk'])
    #     info_class = InformationClassification(application_ptr_id=app.id)
    #     info_class.__dict__.update(app.__dict__)
    #     info_class.save()

    def get_initial(self):
        initial = super(InformationClassificationCreate, self).get_initial()
        initial['app'] = self.kwargs['pk']
        return initial


class InformationClassificationUpdate(SuccessMessageMixin, UpdateView):
    model = InformationClassification
    form_class = InformationClassificationForm
    success_message = 'Information Classification successfully updated!'

    def get_success_url(self):
        return reverse('assessment:informationclassification-detail', kwargs={'pk': self.kwargs['pk']})


class InformationClassificationDelete(SuccessMessageMixin, DeleteView):
    model = InformationClassification
    success_url = reverse_lazy('assessment:application-list')
    success_message = "Information Classification deleted!"


class CloudQuestionnaireDetail(DetailView):
    model = CloudQuestionnaire


class CloudQuestionnaireCreate(SuccessMessageMixin, CreateView):
    model = CloudQuestionnaire
    form_class = CloudQuestionnaireForm
    success_message = 'Cloud Questionnaire successfully saved!'
    success_url = reverse_lazy('assessment:application-list')

    # def post(self, request, *args, **kwargs):
    #     app = Application.objects.get(id=self.kwargs['pk'])
    #     info_class = InformationClassification(application_ptr_id=app.id)
    #     info_class.__dict__.update(app.__dict__)
    #     info_class.save()

    def get_initial(self):
        initial = super(CloudQuestionnaireCreate, self).get_initial()
        initial['app'] = self.kwargs['pk']
        return initial


class CloudQuestionnaireUpdate(SuccessMessageMixin, UpdateView):
    model = CloudQuestionnaire
    form_class = CloudQuestionnaireForm
    success_message = 'Cloud Questionnaire successfully updated!'

    def get_success_url(self):
        return reverse('assessment:cloudquestionnaire-detail', kwargs={'pk': self.kwargs['pk']})


class CloudQuestionnaireDelete(SuccessMessageMixin, DeleteView):
    model = CloudQuestionnaire
    success_url = reverse_lazy('assessment:application-list')
    success_message = "Cloud Questionnaire deleted!"
# class PrivacyAssessmentDetail(DetailView):
#     model = PrivacyAssessment


# class PrivacyAssessmentCreate(SuccessMessageMixin, CreateView):
#     model = PrivacyAssessment
#     form_class = PrivacyAssessmentForm
#     success_message = 'Privacy Assessment successfully saved!'
#     success_url = reverse_lazy('assessment:application-list')

#     def get_initial(self):
#         initial = super(PrivacyAssessmentCreate, self).get_initial()
#         initial['id'] = self.kwargs['pk']
#         return initial


# class PrivacyAssessmentUpdate(SuccessMessageMixin, UpdateView):
#     model = PrivacyAssessment
#     form_class = PrivacyAssessmentForm
#     success_message = 'Privacy Assessment successfully updated!'

#     def get_success_url(self):
#         return reverse('assessment:privacyassessment-detail', kwargs={'pk': self.kwargs['pk']})


# class PrivacyAssessmentDelete(SuccessMessageMixin, DeleteView):
#     model = PrivacyAssessment
#     success_url = reverse_lazy('assessment:application-list')
#     success_message = "Privacy Assessment deleted!"
#     # def delete(self, request, *args, **kwargs):
#     #     obj = self.get_object()
#     #     messages.success(self.request, self.success_message % obj.__dict__)
#     #     return super(ApplicationDelete, self).delete(request, *args, **kwargs)
