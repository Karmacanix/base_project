import datetime
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

# Create your models here.
class ActiveProjectManager(models.Manager):
    def get_queryset(self):
    	return super().get_queryset().filter(status='Active')


class Project(models.Model):
	STATUS_CHOICES = (
		('Active','Active'),
		('On Hold','On Hold'),
		('Closed','Closed'),
	)
	name = models.CharField(max_length=120, help_text="Enter the name of your project")
	desc = models.CharField(max_length=300, verbose_name='Purpose', help_text="Enter a project description")
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="On Hold")
	start_week = models.CharField(max_length=8, help_text="The week the project starts")
	end_week = models.CharField(max_length=8, help_text="The week the project ends")
	billable = models.BooleanField(default=True, help_text="Only billable projects can be invoiced")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	approvers = models.ManyToManyField(User)
	objects = models.Manager()
	active = ActiveProjectManager()
	history = HistoricalRecords()

	class Meta:
		ordering = ["-created"]

	def get_absolute_url(self):
		return reverse('projects:project-detail', kwargs={'pk': self.id})

	def __str__(self):
		return self.name


class Task(models.Model):
	title = models.CharField(max_length=120)
	desc = models.CharField(max_length=300, verbose_name='Description')
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	history = HistoricalRecords()

	class Meta:
		ordering = ["-created"]

	def get_absolute_url(self):
		return reverse('projects:task-detail', kwargs={'pk': self.id})

	def __str__(self):
		return self.title


class Team(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True)
	rate  = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Hourly rate')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	history = HistoricalRecords()

	class Meta:
		ordering = ["-created"]

	def get_absolute_url(self):
		return reverse('projects:team-detail', kwargs={'pk': self.id})

	def __str__(self):
		return self.member.username

