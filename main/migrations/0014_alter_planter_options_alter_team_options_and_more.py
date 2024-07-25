# Generated by Django 5.0.7 on 2024-07-25 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_team_options_remove_team_name_team_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planter',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Planter', 'verbose_name_plural': 'Planters'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['serial'], 'permissions': [('view_history', 'Can View History')], 'verbose_name': 'Team', 'verbose_name_plural': 'Team'},
        ),
        migrations.RemoveField(
            model_name='planter',
            name='model',
        ),
    ]
