# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-24 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20180725_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='booking',
            field=models.ManyToManyField(null=True, to='travel.Booking'),
        ),
    ]
