#from allauth.account.models import EmailAddress
#from django.contrib.auth.models import User
from django import forms
from .models import Application, InformationClassification, CloudQuestionnaire, CloudICTBriefCloudRiskAssessment #, PrivacyAssessment, NonFunctionals

class ApplicationForm(forms.ModelForm):
	
	class Meta:
		model = Application
		fields = ['name', 'purpose', 'application_type', 'website', 'cost', 'cost_type', 'requestor', 'business_owner',]
		widgets = {			
			'name': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'purpose': forms.Textarea(attrs={'class' : 'w3-input w3-border', 'cols': '40', 'rows': '3'}),
			'cost_type': forms.Select(attrs={'class' : 'w3-select w3-border'}),
			'requestor': forms.Select(attrs={'class' : 'w3-select w3-border'}),
			'business_owner': forms.Select(attrs={'class' : 'w3-select w3-border'}),
			'application_type': forms.Select(attrs={'class' : 'w3-select w3-border'}),
			'cost': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'website': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
		}


class InformationClassificationForm(forms.ModelForm):
	
 	class Meta:
 		model = InformationClassification
 		fields = '__all__'
 		widgets = {			
			'special_handling_sensitive_other': forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
			'medical_in_confidence': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'staff_in_confidence': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'commercial_in_confidence': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'statistical_unclassified': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'unclassified': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'special_handling_sensitive_patient': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'special_handling_sensitive_disease': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'special_handling_sensitive_abuse': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		}


class CloudQuestionnaireForm(forms.ModelForm):
	
 	class Meta:
 		model = CloudQuestionnaire
 		fields = '__all__'
 		widgets = {			
			'disclosure_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'alteration_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'loss_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
			'continuity_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		}


class CloudICTBriefCloudRiskAssessmentForm(forms.ModelForm):
	
 	class Meta:
 		model = CloudICTBriefCloudRiskAssessment
 		fields = '__all__'
 	# 	widgets = {			
		# 	'disclosure_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		# 	'alteration_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		# 	'loss_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		# 	'continuity_risk': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		# }


# class PrivacyAssessmentForm(forms.ModelForm):
	
# 	class Meta:
# 		model = PrivacyAssessment
# 		fields = ['application_privacy_policy_URL']


# class NonFunctionalsForm(forms.ModelForm):
	
# 	class Meta:
# 		model = NonFunctionals
# 		fields = ['application_terms_conditions_URL']
		# widgets = {			
		# 	'name': forms.TextInput(attrs={'class' : 'w3-input'}),
		# 	'desc': forms.Textarea(attrs={'class' : 'w3-input w3-border', 'cols': '40', 'rows': '3'}),
		# 	'status': forms.Select(attrs={'class' : 'w3-select'}),
		# 	'billable': forms.CheckboxInput(attrs={'class' : 'w3-check'}),
		# 	'start_week': forms.TextInput(attrs={'type': 'week', 'class' : 'w3-input'}),
		# 	'end_week': forms.TextInput(attrs={'type': 'week', 'class' : 'w3-input'}),
		# 	'customer': forms.Select(attrs={'class' : 'w3-select'}),
		# }