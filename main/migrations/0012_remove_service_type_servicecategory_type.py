# Generated by Django 5.0.6 on 2024-06-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_servicecategory_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='type',
            field=models.CharField(blank=True, choices=[('Commercial', 'Commercial'), ('Residential', 'Residential')], default='Residential', help_text='Select the type of service.', max_length=20, null=True),
        ),
    ]
