# django
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# 3rd party add-ons
from invitations.models import Invitation

# this app
from .models import Project, Task
from .forms import ProjectForm, ProjectApproversForm, TaskForm, TaskFormSet

# Create your views here.
class ProjectList(ListView):
    model = Project

class ProjectDetail(DetailView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm

class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:project-list')

class ProjectApproversCreate(CreateView):
    model = Project
    form_class = ProjectApproversForm

class ProjectApproversUpdate(UpdateView):
    model = Project
    form_class = ProjectApproversForm
    template_name_suffix = '_approvers_form'

class TaskList(ListView):
    model = Task

class TaskDetail(DetailView):
    model = Task

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm