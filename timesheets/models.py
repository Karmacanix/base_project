from django.conf import settings
from django.db import models
from django.urls import reverse
from projects.models import Project, Task

# Create your models here
class WeekTimesheet(models.Model):
	name = models.CharField(max_length=40, unique=True, primary_key=True) # should be week year in the format W01-2018 or similar
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	week_start = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('timesheets:week-detail', kwargs={'pk': self.id})


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

	def get_absolute_url(self):
		return reverse('timesheets:week-line-detail', kwargs={'pk': self.id})