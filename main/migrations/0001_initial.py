# Generated by Django 5.0.6 on 2024-06-05 08:10

import django.db.models.deletion
import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteriorDesignService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Interior Design Service',
                'verbose_name_plural': 'Interior Design Services',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Planter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, unique=True)),
                ('planter_type', models.CharField(choices=[('ceramic', 'Ceramic'), ('plastic', 'Plastic'), ('metal', 'Metal'), ('wood', 'Wood'), ('stone', 'Stone'), ('terracotta', 'Terracotta')], default='ceramic', max_length=20)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('xlarge', 'X-Large')], default='medium', max_length=10)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('inventory', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Planter',
                'verbose_name_plural': 'Planters',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='InteriorDesignServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='services/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.interiordesignservice')),
            ],
            options={
                'verbose_name': 'Interior Design Service Image',
                'verbose_name_plural': 'Interior Design Service Images',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('plant_type', models.CharField(blank=True, choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor'), ('both', 'Both')], default='indoor', max_length=10)),
                ('category', models.CharField(choices=[('flowering', 'Flowering'), ('non-flowering', 'Non-flowering'), ('succulent', 'Succulent'), ('tropical', 'Tropical'), ('herb', 'Herb'), ('fruit', 'Fruit')], default='flowering', max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('care_instructions', models.TextField(blank=True, null=True)),
                ('is_pet_friendly', models.BooleanField(default=True)),
                ('benefits', models.TextField(blank=True, null=True)),
                ('inventory', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Plant',
                'verbose_name_plural': 'Plants',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PlanterImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='planters/')),
                ('planter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.planter')),
            ],
            options={
                'verbose_name': 'Planter Image',
                'verbose_name_plural': 'Planter Images',
            },
        ),
        migrations.CreateModel(
            name='PlantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='plants/')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.plant')),
            ],
            options={
                'verbose_name': 'Plant Image',
                'verbose_name_plural': 'Plant Images',
            },
        ),
    ]
