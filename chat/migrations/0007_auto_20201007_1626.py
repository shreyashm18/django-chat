# Generated by Django 3.0.1 on 2020-10-07 10:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_auto_20201007_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='group_members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
