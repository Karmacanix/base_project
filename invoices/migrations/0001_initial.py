# Generated by Django 2.0.2 on 2018-06-08 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_name', models.CharField(help_text='Enter the trading name of the customer', max_length=120)),
                ('cust_ref', models.CharField(help_text='A reference to help identify the customer', max_length=20)),
                ('attention_to', models.CharField(help_text='Enter a contact name, department or position you wish to address the invoice to', max_length=120)),
                ('address_line_1', models.CharField(help_text='Enter the street number and name', max_length=120)),
                ('address_line_2', models.CharField(help_text='Enter the suburb', max_length=120)),
                ('address_line_3', models.CharField(help_text='Enter the city and post code', max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(help_text="Enter the customer's phone number", max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCustomer',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('trading_name', models.CharField(help_text='Enter the trading name of the customer', max_length=120)),
                ('cust_ref', models.CharField(help_text='A reference to help identify the customer', max_length=20)),
                ('attention_to', models.CharField(help_text='Enter a contact name, department or position you wish to address the invoice to', max_length=120)),
                ('address_line_1', models.CharField(help_text='Enter the street number and name', max_length=120)),
                ('address_line_2', models.CharField(help_text='Enter the suburb', max_length=120)),
                ('address_line_3', models.CharField(help_text='Enter the city and post code', max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(help_text="Enter the customer's phone number", max_length=16)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical customer',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalInvoiceSettings',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('trading_name', models.CharField(help_text='Your trading name', max_length=120)),
                ('address_line_1', models.CharField(help_text='Your street address', max_length=120)),
                ('address_line_2', models.CharField(help_text='Your suburb', max_length=120)),
                ('address_line_3', models.CharField(help_text='Your city and post code', max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(help_text='Your phone number', max_length=16)),
                ('tax_rate', models.PositiveSmallIntegerField()),
                ('tax_number', models.CharField(help_text='Your registered tax number', max_length=20)),
                ('payment_terms', models.TextField()),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical invoice settings',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='InvoiceSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_name', models.CharField(help_text='Your trading name', max_length=120)),
                ('address_line_1', models.CharField(help_text='Your street address', max_length=120)),
                ('address_line_2', models.CharField(help_text='Your suburb', max_length=120)),
                ('address_line_3', models.CharField(help_text='Your city and post code', max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(help_text='Your phone number', max_length=16)),
                ('tax_rate', models.PositiveSmallIntegerField()),
                ('tax_number', models.CharField(help_text='Your registered tax number', max_length=20)),
                ('payment_terms', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]