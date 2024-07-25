# Generated by Django 5.0.7 on 2024-07-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_planter_features_remove_planterimage_planter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideas',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='plantcategory',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='planter',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='plantercategory',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='plantingaccessories',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='plantingaccessoriescategory',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
