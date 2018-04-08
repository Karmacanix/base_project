from django import forms
from django.forms.models import inlineformset_factory
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
	mon = forms.DurationField()
	tue = forms.DurationField()
	wed = forms.DurationField()
	thu = forms.DurationField()
	fri = forms.DurationField()
	sat = forms.DurationField()
	sun = forms.DurationField()

