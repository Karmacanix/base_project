# Generated by Django 2.0.2 on 2018-06-11 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20180609_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('On Hold', 'On Hold'), ('Closed', 'Closed')], default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(help_text='Choose a customer', on_delete=django.db.models.deletion.CASCADE, to='invoices.Customer'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('On Hold', 'On Hold'), ('Closed', 'Closed')], default='Active', max_length=10),
        ),
    ]
