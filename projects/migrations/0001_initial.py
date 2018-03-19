# Generated by Django 2.0.2 on 2018-03-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of your project', max_length=120)),
                ('desc', models.CharField(help_text='Enter a project description', max_length=300, verbose_name='Purpose')),
                ('is_active', models.BooleanField(default=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]