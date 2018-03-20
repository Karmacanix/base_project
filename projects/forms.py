from django import forms
from django.forms.models import inlineformset_factory
from .models import Project, Task
from invitations.models import Invitation

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'desc', 'start', 'end', 'is_active']
		widgets = {
			'desc': forms.Textarea(),
			'start': forms.SelectDateWidget(),
			'end': forms.SelectDateWidget()
		}

class ProjectApproversForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['approvers']
		widgets = {
			'approvers': forms.CheckboxSelectMultiple(),
		}


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'desc', 'project']
		widgets = {
			'desc': forms.Textarea(),
		}

TaskFormSet = inlineformset_factory(Project, Task, form=TaskForm, extra=0, can_delete=True, min_num=1)