from datetime import date, datetime, timedelta
from django.core import exceptions
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse
from projects.models import Project, Task
from timesheets.models import WeekTimesheet, WeekTimesheetLine, WeekTimesheetApprovals, WeekTimesheetLineApprovals
from timesheets.forms import TimesheetLineForm, TimesheetSubmitForm

# Create your views here.
class TimesheetLines(ListView):
	model = WeekTimesheetLine
	template_name = 'timesheets/timesheet_lines.html'
	context_object_name = 'timesheet_lines'

	def get_approver(self, **kwargs):
		try:
			WeekTimesheetApprovals.objects.get(timesheet__name=self.kwargs['timesheet_name'], project_approver=self.request.user, approved=False)
			ts_approval = True
		except:
			ts_approval = False

		return ts_approval

	def get_context_data(self, **kwargs):
		context = super(TimesheetLines, self).get_context_data(**kwargs)
		ts = WeekTimesheet.objects.get(name=self.kwargs['timesheet_name'])
		context['approver'] = self.get_approver()
		context['week_start'] = ts.week_start
		context['status'] = ts.status
		context['timesheet_name'] = ts.name
		context['history'] = ts.history.all()
		context['approval_history'] = WeekTimesheetApprovals.history.filter(timesheet__name=self.kwargs['timesheet_name'])
		context['totals'] = WeekTimesheetLine.objects.filter(timesheet=ts).aggregate(
			mon_total=Sum('mon'),
			tue_total=Sum('tue'),
			wed_total=Sum('wed'),
			thu_total=Sum('thu'),
			fri_total=Sum('fri'),
			sat_total=Sum('sat'),
			sun_total=Sum('sun'))
		return context

	def get_queryset(self):
		try:
			timesheet = WeekTimesheet.objects.get(name=self.kwargs['timesheet_name'])
		except:
			start = datetime.strptime(self.kwargs['timesheet_name'][0:8] + '-1', "%Y-W%W-%w")
			timesheet = WeekTimesheet.objects.create(name=self.kwargs['timesheet_name'], user=self.request.user, week_start=start)

		return WeekTimesheetLine.objects.filter(timesheet=timesheet)


class TimesheetLineCreate(CreateView):
	model = WeekTimesheetLine
	template_name = 'timesheets/timesheet_line_form.html'
	form_class = TimesheetLineForm

	def get_context_data(self, **kwargs):
		context = super(TimesheetLineCreate, self).get_context_data(**kwargs)
		context['timesheet_name'] = self.kwargs['timesheet_name']
		ts = WeekTimesheet.objects.get(name=self.kwargs['timesheet_name'])
		context['week_start'] = ts.week_start
		return context

	def get_initial(self):
		initial = super(TimesheetLineCreate, self).get_initial()
		initial['timesheet'] = self.kwargs['timesheet_name']
		return initial

	def get_success_url(self):
		return reverse('timesheets:timesheet-lines', kwargs={'timesheet_name': self.kwargs['timesheet_name']})


class TimesheetLineEdit(UpdateView):
	model = WeekTimesheetLine
	template_name = 'timesheets/timesheet_line_form.html'
	form_class = TimesheetLineForm

	def get_context_data(self, **kwargs):
		context = super(TimesheetLineEdit, self).get_context_data(**kwargs)
		ts = WeekTimesheet.objects.get(name=self.kwargs['timesheet_name'])
		context['timesheet_name'] = ts.name
		context['week_start'] = ts.week_start
		return context

	def get_success_url(self):
		return reverse('timesheets:timesheet-lines', kwargs={'timesheet_name': self.kwargs['timesheet_name']})


class TimesheetList(ListView):
	model = WeekTimesheet
	template_name = 'timesheets/timesheet_list.html'
	context_object_name = "timesheet_list"

	def get_queryset(self):
		return WeekTimesheet.objects.filter(user=self.request.user)


class TimesheetSubmitConfirm(ListView):
	model = WeekTimesheet
	template_name = 'timesheets/timesheet_submit_confirm.html'
	context_object_name = 'timesheet_submit_confirm'

	def post(self, request, *args, **kwargs):
		ts = self.get_queryset()
		if ts.status == "Submitted":
			ts_approval = WeekTimesheetApprovals.objects.get(timesheet__name=self.kwargs['timesheet_name'], project_approver=request.user)
			ts_approval.approved = True
			ts_approval.save()
			ts_approved_count = WeekTimesheetApprovals.objects.filter(timesheet__name=self.kwargs['timesheet_name'], approved=True).count()
			ts_approvals_count = WeekTimesheetApprovals.objects.filter(timesheet__name=self.kwargs['timesheet_name']).count()
			if ts_approved_count == ts_approvals_count:
				ts.status = 'Approved'
				ts.save()

		if ts.status == "New":
			lines = WeekTimesheetLine.objects.filter(timesheet=ts)
			for line in lines:
				approvers_list = line.project.approvers.all()
				for approver in approvers_list:
					try:
						ts_approval = WeekTimesheetApprovals.objects.get(timesheet=ts, project_approver=approver)
					except:
						ts_approval = WeekTimesheetApprovals.objects.create(timesheet=ts, project_approver=approver)

			ts.status = 'Submitted'
			ts.save()

		return redirect('timesheets:timesheet-list')

	def get_context_data(self, **kwargs):
		context = super(TimesheetSubmitConfirm, self).get_context_data(**kwargs)
		ts = WeekTimesheet.objects.get(name=self.kwargs['timesheet_name'])
		context['week_start'] = ts.week_start
		context['timesheet_name'] = ts.name
		context['totals'] = WeekTimesheetLine.objects.filter(timesheet=ts).aggregate(
			mon_total=Sum('mon'),
			tue_total=Sum('tue'),
			wed_total=Sum('wed'),
			thu_total=Sum('thu'),
			fri_total=Sum('fri'),
			sat_total=Sum('sat'),
			sun_total=Sum('sun'))
		return context

	def get_queryset(self):
		return WeekTimesheet.objects.get(name=self.kwargs['timesheet_name'])

	def get_success_url(self):
		return reverse('timesheets:timesheet-lines', kwargs={'timesheet_name': self.kwargs['timesheet_name']})


class ApprovalList(ListView):
	model = WeekTimesheetApprovals
	template_name = 'timesheets/approval_list.html'
	context_object_name = "approval_list"

	def get_context_data(self, **kwargs):
		context = super(ApprovalList, self).get_context_data(**kwargs)
		context['approval_history'] = WeekTimesheetApprovals.history.filter(project_approver=self.request.user, approved=True).order_by('timesheet')
		return context

	def get_queryset(self):
		return WeekTimesheetApprovals.objects.filter(project_approver=self.request.user, approved=False).order_by('timesheet')