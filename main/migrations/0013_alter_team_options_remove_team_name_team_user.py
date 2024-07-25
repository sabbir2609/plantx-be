# Generated by Django 5.0.7 on 2024-07-25 16:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_testimonial_name_customer_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['serial'], 'permissions': [('view_history', 'Can View History')], 'verbose_name': 'Team Member', 'verbose_name_plural': 'Team Members'},
        ),
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
