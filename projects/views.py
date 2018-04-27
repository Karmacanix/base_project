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
    
    def get_form_kwargs(self):
        kwargs = super(ProjectApproversUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    model = Project
    form_class = ProjectApproversForm
    template_name_suffix = '_approvers_form'


class TaskList(ListView):
    model = Task
    def get_queryset(self):
        queryset = super(TaskList, self).get_queryset()
        queryset = queryset.filter(project=self.kwargs['project'])
        return queryset

class TaskDetail(DetailView):
    model = Task

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm