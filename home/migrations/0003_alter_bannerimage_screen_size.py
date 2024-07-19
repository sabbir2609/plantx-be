# Generated by Django 5.0.6 on 2024-07-19 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_bannerimage_screen_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='screen_size',
            field=models.CharField(choices=[('Small Screen', 'Small Screen'), ('Large Screen', 'Large Screen')], help_text='Select the size of the plant.', max_length=20),
        ),
    ]
