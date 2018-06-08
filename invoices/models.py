from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Customer(models.Model):
	trading_name = models.CharField(max_length=120, help_text="Enter the trading name of the customer")
	cust_ref = models.CharField(max_length=20, help_text="A reference to help identify the customer")
	attention_to = models.CharField(max_length=120, help_text="Enter a contact name, department or position you wish to address the invoice to")
	address_line_1 = models.CharField(max_length=120, help_text="Enter the street number and name")
	address_line_2 = models.CharField(max_length=120, help_text="Enter the suburb")
	address_line_3 = models.CharField(max_length=120, help_text="Enter the city and post code")
	email = models.EmailField()
	phone = models.CharField(max_length=16, help_text="Enter the customer's phone number")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('invoices:customer-detail', kwargs={'pk': self.id})

	def __str__(self):
		return self.trading_name


class InvoiceSettings(models.Model):
	trading_name = models.CharField(max_length=120, help_text="Your trading name")
	address_line_1 = models.CharField(max_length=120, help_text="Your street address")
	address_line_2 = models.CharField(max_length=120, help_text="Your suburb")
	address_line_3 = models.CharField(max_length=120, help_text="Your city and post code")
	email = models.EmailField()
	phone = models.CharField(max_length=16, help_text="Your phone number")
	tax_rate = models.PositiveSmallIntegerField()
	tax_number = models.CharField(max_length=20, help_text="Your registered tax number")
	payment_terms =  models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('invoices:invoice-settings', kwargs={'pk': self.id})

	def __str__(self):
		return self.trading_name

	