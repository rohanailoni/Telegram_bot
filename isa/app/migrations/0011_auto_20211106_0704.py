# Generated by Django 3.2.9 on 2021-11-06 07:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='user_acess',
        ),
        migrations.AddField(
            model_name='document',
            name='user_acess',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
