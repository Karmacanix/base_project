from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project

class ProjectList(ListView):
    model = Project

class ProjectDetail(DetailView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    fields = ['name','desc','start','end']

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name','desc','start','end','is_active']

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects')