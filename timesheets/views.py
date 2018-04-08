from datetime import date, datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from timesheets.models import TimeLog
from timesheets.forms import TimeLogForm

# Create your views here.
class TimeLogList(ListView):
    model = TimeLog

class TimeLogDetail(DetailView):
    model = TimeLog

class TimeLogCreate(CreateView):
    model = TimeLog
    form_class = TimeLogForm

class TimeLogUpdate(UpdateView):
    model = TimeLog
    form_class = TimeLogForm

def WeeklyTimesheetView(request):
	week = str(date.today().isocalendar()[1])
	year = str(date.today().isocalendar()[0])
	if request.POST:
		week_year = request.POST['week_year']
		week = str(week_year[-2])+str(week_year[-1])
		year = str(week_year[0])+str(week_year[1])+str(week_year[2])+str(week_year[3])
		weekly_timelog = TimeLog.objects.filter(work_date__year=year, work_date__week=week)
	else:
		week_year = year+"-W"+week
		weekly_timelog = TimeLog.objects.filter(work_date__year=year, work_date__week=week)
	print("Year: ", year, "Week: ", week)
	week_start = datetime.strptime(week_year + '-1', "%Y-W%W-%w")
	print(week_start)
	days_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	context = {'weekly_timelog': weekly_timelog,
				'week': week,
				'year': year,
				'week_start': week_start,
				'days_of_the_week': days_of_the_week}
	return render(request, 'timesheets/timelog_weekly.html', context)