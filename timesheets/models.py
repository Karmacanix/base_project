from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from projects.models import Project, Task
from simple_history.models import HistoricalRecords

# Create your models here
STATUS_CHOICES = (
		('New','New timesheet'),
		('Submitted','Submitted awaiting approval'),
		('Approved','Approved'),
		('Resubmitted','Resubmitted awaiting approval'),
		('Invoiced','Customer has been invoiced'),
		('Rework','Rework required'),
		('Closed','Closed no longer accepts new data'),
	)

class WeekTimesheet(models.Model):
	name = models.CharField(max_length=40, unique=True, primary_key=True) # should be week year in the format W01-2018 or similar
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	week_start = models.DateField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="New")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	history = HistoricalRecords()

	class Meta:
		ordering = ["-name"]

	def get_absolute_url(self):
		return reverse('timesheets:timesheet-lines', kwargs={'timesheet_name': self.name})

	def __str__(self):
		return self.name


class WeekTimesheetLine(models.Model):
	timesheet = models.ForeignKey(WeekTimesheet, db_column='name', on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	mon = models.DecimalField(max_digits=4, decimal_places=2)
	tue = models.DecimalField(max_digits=4, decimal_places=2)
	wed = models.DecimalField(max_digits=4, decimal_places=2)
	thu = models.DecimalField(max_digits=4, decimal_places=2)
	fri = models.DecimalField(max_digits=4, decimal_places=2)
	sat = models.DecimalField(max_digits=4, decimal_places=2)
	sun = models.DecimalField(max_digits=4, decimal_places=2)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="New")
	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('timesheets:week-line-detail', kwargs={'pk': self.id})


class WeekTimesheetApprovals(models.Model):
	timesheet = models.ForeignKey(WeekTimesheet, on_delete=models.CASCADE)
	project_approver = models.ForeignKey(User, on_delete=models.CASCADE)
	approved = models.BooleanField(default=False)
	rejected = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	history = HistoricalRecords()


class WeekTimesheetLineApprovals(models.Model):
	timesheet_line = models.ForeignKey(WeekTimesheetLine, on_delete=models.CASCADE)
	project_approver = models.ForeignKey(User, on_delete=models.CASCADE)
	approved = models.BooleanField(default=False)
	rejected = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	history = HistoricalRecords()

	def timesheet(self):
		return self.timesheet_line.timesheet.name