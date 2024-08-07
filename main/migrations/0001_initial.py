# Generated by Django 5.0.7 on 2024-08-03 20:48

import django.core.validators
import main.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='customers/', validators=[main.validators.validate_file_size])),
                ('phone', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, help_text='Address of the customer', null=True)),
                ('membership', models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'Gold')], default='B', max_length=1)),
            ],
            options={
                'ordering': ['user__last_name', 'user__first_name'],
                'permissions': [('view_history', 'Can View History')],
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ideas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='ideas/', validators=[main.validators.validate_file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='images/', validators=[main.validators.validate_file_size])),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True)),
                ('inventory', models.PositiveIntegerField(default=1, help_text='Number of items in stock', validators=[django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size', models.CharField(blank=True, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Extra Large', 'Extra Large')], max_length=20)),
                ('location_type', models.CharField(blank=True, choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor'), ('Both', 'Both')], default='Both', max_length=20, null=True)),
                ('care_instructions', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Plant',
                'verbose_name_plural': 'Plants',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PlantCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='plant_categories/', validators=[main.validators.validate_file_size])),
            ],
            options={
                'verbose_name': 'Plant Category',
                'verbose_name_plural': 'Plant Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Planter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True)),
                ('inventory', models.PositiveIntegerField(default=1, help_text='Number of items in stock', validators=[django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size', models.CharField(blank=True, help_text='Size in inches', max_length=20, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('is_custom', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Planter',
                'verbose_name_plural': 'Planters',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='PlanterCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='planter_categories/')),
            ],
            options={
                'verbose_name': 'Planter Category',
                'verbose_name_plural': 'Planter Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PlantingAccessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True)),
                ('inventory', models.PositiveIntegerField(default=1, help_text='Number of items in stock', validators=[django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Planting Accessory',
                'verbose_name_plural': 'Planting Accessories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PlantingAccessoriesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='planting_accessories_categories/')),
            ],
            options={
                'verbose_name': 'Planting Accessory Category',
                'verbose_name_plural': 'Planting Accessory Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('client', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField(blank=True, help_text='Discount in percentage, if any', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.PositiveSmallIntegerField(unique=True)),
                ('type', models.CharField(blank=True, choices=[('Commercial', 'Commercial'), ('Residential', 'Residential')], default='Residential', max_length=20, null=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='service_categories/', validators=[main.validators.validate_file_size])),
            ],
            options={
                'verbose_name': 'Service Category',
                'verbose_name_plural': 'Service Categories',
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.PositiveSmallIntegerField(unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='team_members/', validators=[main.validators.validate_file_size])),
                ('bio', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='TeamContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media_name', models.CharField(max_length=100)),
                ('social_media_link', models.URLField()),
            ],
            options={
                'verbose_name': 'Team Contact',
                'verbose_name_plural': 'Team Contacts',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials/', validators=[main.validators.validate_file_size])),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'ordering': ['-created_at'],
            },
        ),
    ]
