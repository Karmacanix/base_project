# Generated by Django 2.0.2 on 2018-04-27 21:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='approvers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
