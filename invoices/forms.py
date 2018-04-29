from django import forms
from projects.models import Project

class ProjectSelect(forms.Form):

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop("request")
		super(ProjectSelect, self).__init__(*args, **kwargs)
		my_projects = Project.objects.filter(approvers=self.request.user)
		self.fields['project'] = forms.ModelChoiceField(queryset=my_projects, required=True)