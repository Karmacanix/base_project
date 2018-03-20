from django.db import models
from django.urls import reverse
from invitations.models import Invitation

# Create your models here.
class Project(models.Model):
	"""
	A project class 
	"""

	#fields
	name = models.CharField(max_length=120, help_text="Enter the name of your project")
	desc = models.CharField(max_length=300, verbose_name='Purpose', help_text="Enter a project description")
	is_active = models.BooleanField(default=True)
	start = models.DateField()
	end = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	approvers = models.ManyToManyField(Invitation)

	#metadata
	class Meta:
		ordering = ["-created"]

	#methods
	def get_absolute_url(self):
		return reverse('projects:project-detail', kwargs={'pk': self.id})

	def __str__(self):
		"""
		String for representing the project object (in Admin site etc.)
		"""
		return self.name


class Task(models.Model):
	"""
	A task class 
	"""

	#fields
	title = models.CharField(max_length=120)
	desc = models.CharField(max_length=300, verbose_name='Description')
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	#metadata
	class Meta:
		ordering = ["-created"]

	#methods
	def get_absolute_url(self):
		return reverse('projects:task-detail', kwargs={'pk': self.id})

	def __str__(self):
		"""
		String for representing the project object (in Admin site etc.)
		"""
		return self.title

