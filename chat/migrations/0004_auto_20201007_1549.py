# Generated by Django 3.0.1 on 2020-10-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20201007_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='group_members',
            field=models.ManyToManyField(to='chat.Participants'),
        ),
    ]
