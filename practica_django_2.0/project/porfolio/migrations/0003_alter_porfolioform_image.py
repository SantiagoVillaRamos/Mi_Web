# Generated by Django 5.0.7 on 2024-08-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0002_alter_porfolioform_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porfolioform',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Imagen'),
        ),
    ]
