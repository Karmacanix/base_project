# Generated by Django 2.0.2 on 2018-04-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0005_auto_20180419_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weektimesheet',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
