from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from timesheets.models import TimeLog
from timesheets.forms import TimeLogForm

# Create your views here.
class TimeLogList(ListView):
    model = TimeLog

class TimeLogDetail(DetailView):
    model = TimeLog

class TimeLogCreate(CreateView):
    model = TimeLog
    form_class = TimeLogForm

class TimeLogUpdate(UpdateView):
    model = TimeLog
    form_class = TimeLogForm