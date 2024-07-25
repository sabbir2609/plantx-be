# Generated by Django 5.0.7 on 2024-07-25 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_ideas_slug_plantcategory_slug_planter_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantcategory',
            name='featured_plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.plant'),
        ),
        migrations.AddField(
            model_name='plantercategory',
            name='featured_planter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.planter'),
        ),
    ]
