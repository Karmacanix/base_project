# django
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

# 3rd party add-ons
from invitations.models import Invitation

# this app
from .models import Project, Task, Team
from .forms import ProjectForm, ProjectApproversForm, TaskForm, TeamForm

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


class TeamList(ListView):
    model = Team

    def get_queryset(self):
        queryset = super(TeamList, self).get_queryset()
        queryset = queryset.filter(project=self.kwargs['project_id'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TeamList, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs['project_id']
        return context


class TeamDetail(DetailView):
    model = Team


class TeamCreate(CreateView):
    model = Team
    template_name = 'projects/team_form.html'
    form_class = TeamForm

    def get_initial(self):
        initial = super(TeamCreate, self).get_initial()
        initial['project'] = self.kwargs['project_id']
        return initial

    def get_form_kwargs(self):
        kwargs = super(TeamCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse('projects:team-list', kwargs={'project_id': self.kwargs['project_id']})

    def get_context_data(self, **kwargs):
        context = super(TeamCreate, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs['project_id']
        return context


class TeamUpdate(UpdateView):
    model = Team
    template_name = 'projects/team_form.html'
    form_class = TeamForm

    def get_form_kwargs(self):
        kwargs = super(TeamUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(TeamUpdate, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs['project_id']
        return context

    def get_success_url(self):
        return reverse('projects:team-list', kwargs={'project_id': self.kwargs['project_id']})