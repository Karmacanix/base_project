from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserInvoiceProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trading_name = models.CharField(max_length=240)
    street_address = models.CharField(max_length=240)
    suburb  = models.CharField(max_length=240)
    city_town  = models.CharField(max_length=240)
    postcode  = models.CharField(max_length=240)
    phone = models.CharField(max_length=240)
    logo  = models.CharField(max_length=240) # users business logo
    gst_rate = models.CharField(max_length=240)#percent of GST
    gst_number =  models.CharField(max_length=240)# number issued by inland revenue for display on invoices
    payment_terms = models.CharField(max_length=400) # shoudl be a text area