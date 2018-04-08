from django import forms
from django.forms.formsets import formset_factory
from django.forms.widgets import NumberInput
from projects.models import Project, Task
from timesheets.models import TimeLog

class TimeLogForm(forms.ModelForm):
	class Meta:
		model = TimeLog
		fields = ['project', 'task', 'user', 'duration', 'work_date']
		widgets = {
			'work_date': forms.SelectDateWidget(),
		}

class WeeklyTimesheetForm(forms.Form):
	project = forms.ModelChoiceField(queryset=Project.objects.all())
	task = forms.ModelChoiceField(queryset=Task.objects.all())
	mon = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	tue = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	wed = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	thu = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	fri = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	sat = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	sun = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))

WeeklyTimesheetFormset = formset_factory(WeeklyTimesheetForm, extra=1, can_order=False, can_delete=True, max_num=70, validate_max=True, min_num=1, validate_min=True)