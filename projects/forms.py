from django import forms
from .models import Project

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
	template_name = "project_approvers_form.html"
	class Meta:
		model = Project
		fields = ['approvers']
		widgets = {
			'approvers': forms.CheckboxSelectMultiple(),
		}