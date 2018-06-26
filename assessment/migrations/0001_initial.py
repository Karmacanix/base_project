# Generated by Django 2.0.2 on 2018-06-25 08:04

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
            name='Application',
            fields=[
                ('name', models.CharField(max_length=254, primary_key=True, serialize=False, verbose_name='Application Name')),
                ('website', models.URLField(verbose_name='Application Website')),
                ('purpose', models.CharField(max_length=254, verbose_name='Application Purpose')),
                ('cost', models.CharField(max_length=254, verbose_name='Application Cost')),
                ('cost_type', models.CharField(choices=[('1', 'One time payment'), ('M', 'Monthly'), ('Y', 'Annually')], default='Y', max_length=1, verbose_name='payment frequency')),
                ('business_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_owner', to=settings.AUTH_USER_MODEL, verbose_name='Business Owner (cost centre owner)')),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestor', to=settings.AUTH_USER_MODEL, verbose_name='Requestor (application user)')),
            ],
        ),
    ]
