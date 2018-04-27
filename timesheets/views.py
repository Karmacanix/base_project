from datetime import date, datetime, timedelta
from django.core import exceptions
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from projects.models import Project, Task
from timesheets.models import WeekTimesheet, WeekTimesheetLine
from timesheets.forms import TimesheetLineForm

# Create your views here.
class TimesheetLines(ListView):
	model = WeekTimesheetLine
	template_name = 'timesheets/timesheet_lines.html'
	context_object_name = "timesheet_lines"

	def get_context_data(self, **kwargs):
		context = super(TimesheetLines, self).get_context_data(**kwargs)
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


def timesheet_select(request):
	return render(request, template_name='timesheets/timesheet_select.html')