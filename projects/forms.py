from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from django import forms
from .models import Project, Task, Team
from invoices.models import Customer
from invitations.models import Invitation

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'desc', 'status', 'billable', 'start_week', 'end_week', 'customer', 'owner']
		widgets = {
			'desc': forms.Textarea(),
			'start_week': forms.TextInput(attrs={'type': 'week'}),
			'end_week': forms.TextInput(attrs={'type': 'week'})
		}

class ProjectApproversForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		super(ProjectApproversForm, self).__init__(*args, **kwargs)

		my_invites = Invitation.objects.filter(inviter=self.user).values_list('email', flat=True)
		invite_email_list = list(EmailAddress.objects.filter(email__in=my_invites).values_list('user', flat=True))
		invite_email_list.append(self.user.id)
		APPROVERS_LIST = User.objects.filter(id__in=invite_email_list)
		
		self.fields['approvers'] = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=APPROVERS_LIST, required=True)


	class Meta:
		model = Project
		fields = ['approvers']


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'desc', 'project']
		widgets = {
			'desc': forms.Textarea(),
		}


class TeamForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		super(TeamForm, self).__init__(*args, **kwargs)

		my_invites = Invitation.objects.filter(inviter=self.user).values_list('email', flat=True)
		invite_email_list = list(EmailAddress.objects.filter(email__in=my_invites).values_list('user', flat=True))
		invite_email_list.append(self.user.id)
		APPROVERS_LIST = User.objects.filter(id__in=invite_email_list)
		
		self.fields['member'] = forms.ModelChoiceField(queryset=APPROVERS_LIST, required=True)

	class Meta:
		model = Team
		fields = ['project', 'member', 'is_active', 'rate']