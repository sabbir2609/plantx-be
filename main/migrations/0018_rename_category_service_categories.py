# Generated by Django 5.0.6 on 2024-07-10 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_service_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='category',
            new_name='categories',
        ),
    ]
