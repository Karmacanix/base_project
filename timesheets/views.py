from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from projects.models import Project, Task
from timesheets.models import TimeLog
from timesheets.forms import TimeLogForm, WeeklyTimesheetForm, WeeklyTimesheetFormset

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
	tue_date = week_start + timedelta(days=1)
	wed_date = week_start + timedelta(days=2)
	thu_date = week_start + timedelta(days=3)
	fri_date = week_start + timedelta(days=4)
	sat_date = week_start + timedelta(days=5)
	sun_date = week_start + timedelta(days=6)
	print(tue_date, wed_date, thu_date, fri_date, sat_date, sun_date)
	days_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	dates_of_the_week = [tue_date, wed_date, thu_date, fri_date, sat_date, sun_date]
	timesheet_form = WeeklyTimesheetForm()
	timesheet_formset = WeeklyTimesheetFormset(prefix="timesheet")
	context = {'weekly_timelog': weekly_timelog,
				'week_year': week_year,
				'week': week,
				'year': year,
				'week_start': week_start,
				'days_of_the_week': days_of_the_week,
				'dates_of_the_week': dates_of_the_week,
				'timesheet_form': timesheet_form,
				'timesheet_formset': timesheet_formset}
	return render(request, 'timesheets/timelog_weekly.html', context)

def WeeklyTimesheetFormView(request):
	
	if request.POST:
		week_year = request.POST['week_year']
		week_start = datetime.strptime(week_year + '-1', "%Y-W%W-%w")
		mon_date = week_start.strftime("%Y-%m-%d")
		week_start_tue = week_start + timedelta(days=1)
		tue_date = week_start_tue.strftime("%Y-%m-%d")
		week_start_wed = week_start + timedelta(days=2)
		wed_date = week_start_wed.strftime("%Y-%m-%d")
		week_start_thu = week_start + timedelta(days=3)
		thu_date = week_start_thu.strftime("%Y-%m-%d")
		week_start_fri = week_start + timedelta(days=4)
		fri_date = week_start_fri.strftime("%Y-%m-%d")
		week_start_sat = week_start + timedelta(days=5)
		sat_date = week_start_sat.strftime("%Y-%m-%d")
		week_start_sun = week_start + timedelta(days=6)
		sun_date = week_start_sun.strftime("%Y-%m-%d")
		week = str(week_year[-2])+str(week_year[-1])
		year = str(week_year[0])+str(week_year[1])+str(week_year[2])+str(week_year[3])
		weekly_timelog = TimeLog.objects.filter(work_date__year=year, work_date__week=week, user=request.user)
		mon_value=0.0
		tue_value=0.0
		wed_value=0.0
		thu_value=0.0
		fri_value=0.0
		sat_value=0.0
		sun_value=0.0
		for entry in weekly_timelog:
			print(entry.project)
			if entry.duration > 0.0:
				print("duration:", entry.duration, "work date:", entry.work_date, "week start:", week_start, "mon:", mon_date, "tue:", tue_date)
				wd = str(entry.work_date)
				dur = float(entry.duration)
				if wd == mon_date:
					mon_value = mon_value + dur
					print("mon true")
				elif wd == tue_date:
					tue_value = tue_value + dur
					print("tue true")
				elif wd == wed_date:
					wed_value = wed_value + dur
					print("w true")
				elif wd == thu_date:
					thu_value = thu_value + dur
					print("th true")
				elif wd == fri_date:
					fri_value = fri_value + dur
					print("fr true")
				elif wd == sat_date:
					sat_value = sat_value + dur
					print("sa true")
				elif wd == sun_date:
					sun_value = sun_value + dur
					print("su true")
				else:
					print("no if statements used")
		
		print(mon_value, tue_value, wed_value, thu_value, fri_value, sat_value, sun_value)
		timesheet_form = WeeklyTimesheetForm(request.POST)
		if timesheet_form.is_valid():
			print("valid")
			if float(timesheet_form['mon'].value()) > 0.00:
				mon = TimeLog(
					project=Project.objects.get(id=timesheet_form['project'].value()),
					task=Task.objects.get(id=timesheet_form['task'].value()),
					duration=timesheet_form['mon'].value(),
					work_date=week_start,
					user=request.user,
					)
				mon.save()
			if float(timesheet_form['tue'].value()) > 0.00:
				tue = TimeLog(
					project=Project.objects.get(id=timesheet_form['project'].value()),
					task=Task.objects.get(id=timesheet_form['task'].value()),
					duration=timesheet_form['tue'].value(),
					work_date=week_start + timedelta(days=1),
					user=request.user,
					)
				tue.save()
			if float(timesheet_form['wed'].value()) > 0.00:
				wed = TimeLog(
					project=Project.objects.get(id=timesheet_form['project'].value()),
					task=Task.objects.get(id=timesheet_form['task'].value()),
					duration=timesheet_form['wed'].value(),
					work_date=week_start + timedelta(days=2),
					user=request.user,
					)
				wed.save()
			if float(timesheet_form['thu'].value()) > 0.00:
				thu = TimeLog(
					project=Project.objects.get(id=timesheet_form['project'].value()),
					task=Task.objects.get(id=timesheet_form['task'].value()),
					duration=timesheet_form['thu'].value(),
					work_date=week_start + timedelta(days=3),
					user=request.user,
					)
				thu.save()
			if float(timesheet_form['fri'].value()) > 0.00:
				fri = TimeLog(
					project=Project.objects.get(id=timesheet_form['project'].value()),
					task=Task.objects.get(id=timesheet_form['task'].value()),
					duration=timesheet_form['fri'].value(),
					work_date=week_start + timedelta(days=4),
					user=request.user,
					)
				fri.save()
			if float(timesheet_form['sat'].value()) > 0.00:
				sat = TimeLog(
					project=Project.objects.get(id=timesheet_form['project'].value()),
					task=Task.objects.get(id=timesheet_form['task'].value()),
					duration=timesheet_form['sat'].value(),
					work_date=week_start + timedelta(days=5),
					user=request.user,
					)
				sat.save()
			if float(timesheet_form['sun'].value()) > 0.00:
				sun = TimeLog(
					project=Project.objects.get(id=timesheet_form['project'].value()),
					task=Task.objects.get(id=timesheet_form['task'].value()),
					duration=timesheet_form['sun'].value(),
					work_date=week_start + timedelta(days=6),
					user=request.user,
					)
				sun.save()
		else:
			timesheet_form = WeeklyTimesheetForm()
	context = {'week_year': week_year,
				'week_start': week_start,
				'timesheet_form': timesheet_form,
				'weekly_timelog': weekly_timelog}
	return render(request, 'timesheets/timelog_week_form.html', context)