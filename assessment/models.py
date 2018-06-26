from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy, reverse

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
	special_handling_sensitive_other = models.CharField(max_length=200, help_text="Other")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class CloudQuestionnaire(models.Model):
	app = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
	disclosure_risk = models.BooleanField(default=False, verbose_name='Information Disclosure Risk')
	alteration_risk = models.BooleanField(default=False, verbose_name='Information Alteration Risk')
	loss_risk = models.BooleanField(default=False, verbose_name='Information Loss Risk')
	continuity_risk = models.BooleanField(default=False, verbose_name='Business Continuity Risk')
