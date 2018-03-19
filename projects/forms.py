from django import forms
from .models import Project
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