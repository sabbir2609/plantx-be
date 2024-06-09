# Generated by Django 5.0.6 on 2024-06-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_plant_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantcategory',
            name='description',
            field=models.TextField(blank=True, help_text='Provide a description for the plant category.', null=True),
        ),
        migrations.AlterField(
            model_name='plantcategory',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload an image for the plant category.', null=True, upload_to='plant_categories/'),
        ),
    ]
