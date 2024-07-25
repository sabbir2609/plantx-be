# Generated by Django 5.0.7 on 2024-07-25 09:22

import django.core.validators
import django.db.models.deletion
import main.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0008_plantingaccessoriescategory_remove_plant_unit_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planter',
            name='features',
        ),
        migrations.RemoveField(
            model_name='planterimage',
            name='planter',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='features',
        ),
        migrations.RemoveField(
            model_name='plantimage',
            name='plant',
        ),
        migrations.RemoveField(
            model_name='plantingaccessoriesimage',
            name='planting_accessory',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='project',
        ),
        migrations.RemoveField(
            model_name='serviceimage',
            name='service',
        ),
        migrations.AddField(
            model_name='planter',
            name='name',
            field=models.CharField(default='some', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plant',
            name='inventory',
            field=models.PositiveIntegerField(default=1, help_text='Number of items in stock', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='planter',
            name='inventory',
            field=models.PositiveIntegerField(default=1, help_text='Number of items in stock', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='plantercategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='planter_categories/'),
        ),
        migrations.AlterField(
            model_name='plantingaccessoriescategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='planting_accessories_categories/'),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='images/', validators=[main.validators.validate_file_size])),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.DeleteModel(
            name='PlanterFeatures',
        ),
        migrations.DeleteModel(
            name='PlanterImage',
        ),
        migrations.DeleteModel(
            name='PlantFeatures',
        ),
        migrations.DeleteModel(
            name='PlantImage',
        ),
        migrations.DeleteModel(
            name='PlantingAccessoriesImage',
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
        migrations.DeleteModel(
            name='ServiceImage',
        ),
    ]