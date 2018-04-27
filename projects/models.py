import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=120, help_text="Enter the name of your project")
	desc = models.CharField(max_length=300, verbose_name='Purpose', help_text="Enter a project description")
	start_week = models.CharField(max_length=8, help_text="The week the project starts")
	end_week = models.CharField(max_length=8, help_text="The week the project ends")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	approvers = models.ManyToManyField(User)

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

	class Meta:
		ordering = ["-created"]

	def get_absolute_url(self):
		return reverse('projects:task-detail', kwargs={'pk': self.id})

	def __str__(self):
		return self.title

