# django
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# this app
from .models import Project
from .forms import ProjectForm, ProjectApproversForm

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