# Generated by Django 2.0.2 on 2018-04-18 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0003_weektimesheet_weektimesheetline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weektimesheet',
            name='week_number',
        ),
        migrations.RemoveField(
            model_name='weektimesheet',
            name='year',
        ),
    ]
