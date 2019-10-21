# Generated by Django 2.0.2 on 2018-06-25 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0004_auto_20180626_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudQuestionnaire',
            fields=[
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='assessment.Application')),
                ('disclosure_risk', models.BooleanField(default=False, verbose_name='Information Disclosure Risk')),
                ('alteration_risk', models.BooleanField(default=False, verbose_name='Information Alteration Risk')),
                ('loss_risk', models.BooleanField(default=False, verbose_name='Information Loss Risk')),
                ('continuity_risk', models.BooleanField(default=False, verbose_name='Business Continuity Risk')),
            ],
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='commercial_in_confidence',
            field=models.BooleanField(default=False, help_text='Commercially sensitive information that needs protection from unauthorised access'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='medical_in_confidence',
            field=models.BooleanField(default=False, help_text='Personal health information'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='special_handling_sensitive_abuse',
            field=models.BooleanField(default=False, help_text='Sensitive subjects (violence and abuse; pandemics)'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='special_handling_sensitive_disease',
            field=models.BooleanField(default=False, help_text='Sensitive categories of disease (eg Mental Health)'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='special_handling_sensitive_other',
            field=models.CharField(help_text='Other', max_length=200),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='special_handling_sensitive_patient',
            field=models.BooleanField(default=False, help_text='Sensitive patient information (eg VIP’s)'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='staff_in_confidence',
            field=models.BooleanField(default=False, help_text='Identifiable employee and practitioner information that is not intended for the public domain'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='statistical_unclassified',
            field=models.BooleanField(default=False, help_text='Statistical or financial information that is non–identifiable'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='unclassified',
            field=models.BooleanField(default=False, help_text='All other information'),
        ),
    ]