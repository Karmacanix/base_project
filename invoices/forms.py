from datetime import date
from django import forms
from projects.models import Project
from invoices.models import Customer, InvoiceSettings


class invoice_parameters(forms.Form):
	current_week = str(date.today().isocalendar()[1])
	current_year = str(date.today().isocalendar()[0])
	value = current_year+"-W"+current_week
	week = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'w3-input', 'type': 'week', 'value': value}))
	project = forms.ModelChoiceField(queryset=Project.active.filter(billable=True), required=True, empty_label="Choose a project", widget=forms.Select(attrs={'class' : 'w3-input'}))


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'


class InvoiceSettingsForm(forms.ModelForm):
	class Meta:
		model = InvoiceSettings
		fields = '__all__'