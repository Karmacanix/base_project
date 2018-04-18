from django import forms
from django.forms.formsets import formset_factory
from django.forms.widgets import NumberInput
from django_select2.forms import Select2Widget, ModelSelect2Widget
from projects.models import Project, Task
from timesheets.models import TimeLog

class TimeLogForm(forms.ModelForm):
	project = forms.ModelChoiceField(
		queryset=Project.objects.all(),
		widget=ModelSelect2Widget(
			model=Project,
			search_fields=['name__icontains'],
			)
		)
	task = forms.ModelChoiceField(
		queryset=Task.objects.all(),
		widget=ModelSelect2Widget(
			model=Task,
			search_fields=['title__icontains'],
			dependent_fields={'project': 'project'},
			max_results=30,
			)
		)
	duration = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	class Meta:
		model = TimeLog
		fields = ['project', 'task', 'user', 'duration', 'work_date']
		widgets = {
			'work_date': forms.SelectDateWidget(),
		}

class WeeklyTimesheetForm(forms.Form):
	project = forms.ModelChoiceField(
		queryset=Project.objects.all(),
		required=True,
		widget=ModelSelect2Widget(
			model=Project,
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
	mon = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	tue = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	wed = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	thu = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	fri = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	sat = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))
	sun = forms.DecimalField(initial=0, max_value=24.00, min_value=0.00, max_digits=4, decimal_places=2, widget = NumberInput(attrs={'step': '0.25'}))

WeeklyTimesheetFormset = formset_factory(WeeklyTimesheetForm, extra=1, can_delete=True, max_num=70, min_num=1)