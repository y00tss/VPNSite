# Generated by Django 4.2.7 on 2023-11-15 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_proxy_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebSites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50, verbose_name='Site name')),
                ('site_url', models.URLField(verbose_name='Site url')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
        ),
    ]