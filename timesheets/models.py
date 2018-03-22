from django.conf import settings
from django.db import models
from django.urls import reverse
from projects.models import Project, Task

# Create your models here
class TimeLog(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	duration = models.DurationField()
	work_date = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('timesheets:timelog-detail', kwargs={'pk': self.id})