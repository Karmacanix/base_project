from django import forms
from django.conf import settings
from django.forms.widgets import NumberInput
from django_select2.forms import ModelSelect2Widget
from projects.models import Project, Task
from timesheets.models import WeekTimesheet, WeekTimesheetLine

class TimesheetLineForm(forms.ModelForm):
	timesheet = forms.ModelChoiceField(
		queryset=WeekTimesheet.objects.all())
	project = forms.ModelChoiceField(
		queryset=Project.active.all(),
		required=True,
		widget=ModelSelect2Widget(
			queryset=Project.active.all(),
			search_fields=['name__icontains'],
			attrs={
				'style': 'width:100%',
				})
	)
	task = forms.ModelChoiceField(
		queryset=Task.objects.all(),
		required=True,
		widget=ModelSelect2Widget(
			model=Task,
			search_fields=['title__icontains'],
			dependent_fields={'project': 'project'},
			max_results=30,
			attrs={
				'style': 'width:100%',
				})
	)
	mon = forms.DecimalField(initial=0.00, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	tue = forms.DecimalField(initial=0.00, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	wed = forms.DecimalField(initial=0.00, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	thu = forms.DecimalField(initial=0.00, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	fri = forms.DecimalField(initial=0.00, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	sat = forms.DecimalField(initial=0.00, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	sun = forms.DecimalField(initial=0.00, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	class Meta:
		model = WeekTimesheetLine
		fields = ['timesheet', 'project', 'task', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']


class TimesheetSubmitForm(forms.ModelForm):
	
	class Meta:
		model = WeekTimesheet
		fields = ['name', 'status', 'user',]