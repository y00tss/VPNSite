# Generated by Django 4.2.7 on 2024-02-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_statistic_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websites',
            name='site_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Site name'),
        ),
        migrations.AlterField(
            model_name='websites',
            name='site_url',
            field=models.CharField(unique=True, verbose_name='Site url'),
        ),
    ]
