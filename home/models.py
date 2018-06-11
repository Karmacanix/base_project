from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class AccountDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	project_admin = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_account_details(sender, instance, created, **kwargs):
	if created:
		AccountDetails.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_account_details(sender, instance, **kwargs):
	instance.accountdetails.save()