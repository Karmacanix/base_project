from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils.functional import curry

# Create your models here.
class Application(models.Model):
	requestor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requestor")
	business_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="business_owner")
	name = models.CharField(max_length=254, primary_key=True)
	website = models.URLField(max_length=200)
	purpose = models.CharField(max_length=254)
	cost = models.CharField(max_length=254)
	COST_CHOICES = (
		('1', 'One time payment'),
		('M', 'Monthly'),
		('Y', 'Annually'),
	)
	cost_type = models.CharField(
		max_length=1,
		choices=COST_CHOICES,
		default='Y',
		verbose_name="Renewal"
	)
	APPLICATION_CHOICES = (
		('C', 'Cloud'),
		('M', 'Mobile'),
		('D', 'Desktop'),
		('T', 'Tablet'),
		('H', 'Hybrid'),
	)
	application_type = models.CharField(
		max_length=1,
		choices=APPLICATION_CHOICES,
		default='C',
		verbose_name="Type"
	)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('assessment:application-detail', kwargs={'pk': self.name})


class InformationClassification(models.Model):
	app = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
	medical_in_confidence = models.BooleanField(default=False, help_text="Personal health information")
	staff_in_confidence = models.BooleanField(default=False, help_text="Identifiable employee and practitioner information that is not intended for the public domain")
	commercial_in_confidence = models.BooleanField(default=False, help_text="Commercially sensitive information that needs protection from unauthorised access")
	statistical_unclassified = models.BooleanField(default=False, help_text="Statistical or financial information that is non–identifiable")
	unclassified = models.BooleanField(default=False, help_text="All other information")
	special_handling_sensitive_patient = models.BooleanField(default=False, help_text="Sensitive patient information (eg VIP’s)")
	special_handling_sensitive_disease = models.BooleanField(default=False, help_text="Sensitive categories of disease (eg Mental Health)")
	special_handling_sensitive_abuse = models.BooleanField(default=False, help_text="Sensitive subjects (violence and abuse; pandemics)")
	special_handling_sensitive_other = models.CharField(max_length=200, blank=False, help_text="Other")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class CloudQuestionnaire(models.Model):
	app = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
	disclosure_risk = models.BooleanField(default=False, verbose_name='Information Disclosure Risk', help_text="The information is publicly available or it can be de-identified so that its release into the public domain would not compromise our obligations to a person or an organisation.")
	alteration_risk = models.BooleanField(default=False, verbose_name='Information Alteration Risk', help_text="No person or organisation will be harmed if the information is altered by mistake or intentionally by a wrongdoer.")
	loss_risk = models.BooleanField(default=False, verbose_name='Information Loss Risk', help_text="No person or orginastion will be harmed if the information is lost by the cloud provider; OR we can easily maintain a local copy of the information.")
	continuity_risk = models.BooleanField(default=False, verbose_name='Business Continuity Risk', help_text="We will be able to carry on our activities if the service is disrupted or is unavailable for an extended.")

	def _get_help_text(self, field_name):

		for field in self._meta.fields:
			if field.name == field_name:
				return field.help_text
	
	def _get_verbose_name(self, field_name):

		for field in self._meta.fields:
			if field.name == field_name:
				return field.verbose_name

	def __init__(self, *args, **kwargs):
		super(CloudQuestionnaire, self).__init__(*args, **kwargs)

		for field in self._meta.fields:
			method_name = "get_{0}_help_text".format(field.name)
			curried_method = curry(self._get_help_text, field_name=field.name)
			setattr(self, method_name, curried_method)
			method_v_name = "get_{0}_verbose_name".format(field.name)
			curried_v_method = curry(self._get_verbose_name, field_name=field.name)
			setattr(self, method_v_name, curried_v_method)


class CloudICTBriefCloudRiskAssessment(models.Model):
	app = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
	termsconditions_URL = models.URLField(help_text="Please copy and paste the apps terms and conditions from the vendors website. Make sure you get the T&Cs for the version of the app you want.")
	privacypolicy_URL = models.URLField(help_text="Please copy and paste the apps privacy policy from the vendors website. Make sure you get the privacy policy for the version of the app you want.")
	RECORD_CHOICES = (
		('TENS', '10s'),
		('HUNDREDS', '100s'),
		('THOUSANDS', '1,000s'),
		('TENTHOUSANDS', '10,000s'),
		('HUNDREDTHOUSANDS', '100,000s'),
	)
	dhb_record_volume = models.CharField(max_length=15, choices=RECORD_CHOICES, default='TENS', help_text="Provide an estimate of the number of records we expect to store in the application on an annual basis.")
	DOWNTIME_CHOICES = (
		('H', 'Hours'),
		('D', 'Days'),
		('M', 'Months'),
		('I', 'Indefinitely')
	)
	dhb_downtime_before_critical = models.CharField(max_length=1, choices=DOWNTIME_CHOICES, default='H', help_text="We can be without this app before our service can no longer function properly. Specify the time interval.")
	UNSURE_CHOICES = (
		('Y', 'Yes'),
		('N', 'No'),
		('U', 'Unsure'),
	)
	dhb_log_data_changes = models.CharField(max_length=1, choices=UNSURE_CHOICES, default='U', help_text="We will be able to notice if someone accidentally or maliously alters our data stored in the cloud service.")

	def _get_help_text(self, field_name):

		for field in self._meta.fields:
			if field.name == field_name:
				return field.help_text
	
	def __init__(self, *args, **kwargs):
		super(CloudICTBriefCloudRiskAssessment, self).__init__(*args, **kwargs)

		for field in self._meta.fields:
			method_name = "get_{0}_help_text".format(field.name)
			curried_method = curry(self._get_help_text, field_name=field.name)
			setattr(self, method_name, curried_method)