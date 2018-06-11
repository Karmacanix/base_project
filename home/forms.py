from datetime import date
from django import forms
from home.models import AccountDetails


class AccountDetailsForm(forms.ModelForm):
	class Meta:
		model = AccountDetails
		fields = '__all__'