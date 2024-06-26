# Generated by Django 5.0.6 on 2024-06-20 01:55

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Add tags that describe the plant.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='plantimage',
            name='short_description',
            field=models.CharField(blank=True, help_text='Enter a short description for the plant image.', max_length=255, null=True),
        ),
    ]
