from datetime import date, datetime, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from reportlab.pdfgen import canvas
from projects.models import Project, Team
from timesheets.models import WeekTimesheet, WeekTimesheetLine
from invoices.models import Customer, InvoiceSettings
from invoices.forms import invoice_parameters, CustomerForm, InvoiceSettingsForm

# Create your views here.
class InvoiceParams(FormView):
	form_class = invoice_parameters
	template_name = 'invoices/invoice_params.html'

	def post(self, request, *args, **kwargs):
		"""Handle GET requests: instantiate a blank version of the form."""
		form = self.get_form()
		form.is_valid()
		return redirect('invoices:invoice', form.cleaned_data['week'], form.cleaned_data['project'], form.cleaned_data['settings'])


class Invoice(ListView):
	model = WeekTimesheet
	template_name = 'invoices/invoice.html'
	context_object_name = 'invoice'

	def get_context_data(self, **kwargs):
		context = super(Invoice, self).get_context_data(**kwargs)
		ts = self.get_queryset().values_list('name', flat=True)
		us = self.get_queryset().values_list('user', flat=True)
		context['p'] = self.kwargs['project']
		context['week'] = self.kwargs['week']
		context['settings'] = InvoiceSettings.objects.get(trading_name=self.kwargs['settings'])
		context['timesheet_lines'] = WeekTimesheetLine.objects.filter(project__name=self.kwargs['project'],timesheet__in=ts)
		context['team'] = Team.objects.filter(project__name=self.kwargs['project'], member__in=us)
		return context

	def get_queryset(self):
		start = datetime.strptime(self.kwargs['week'][0:8] + '-1', "%Y-W%W-%w")
		return WeekTimesheet.objects.filter(week_start=start, status='Approved')


class CustomerList(ListView):
    model = Customer


class CustomerDetail(DetailView):
    model = Customer


class CustomerCreate(CreateView):
    model = Customer
    form_class = CustomerForm


class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CustomerForm


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('invoices:customer-list')


class InvoiceSettingsList(ListView):
    model = InvoiceSettings


class InvoiceSettingsDetail(DetailView):
    model = InvoiceSettings


class InvoiceSettingsCreate(CreateView):
    model = InvoiceSettings
    form_class = InvoiceSettingsForm


class InvoiceSettingsUpdate(UpdateView):
    model = InvoiceSettings
    form_class = InvoiceSettingsForm


class InvoiceSettingsDelete(DeleteView):
    model = InvoiceSettings
    success_url = reverse_lazy('invoices:settings-list')
