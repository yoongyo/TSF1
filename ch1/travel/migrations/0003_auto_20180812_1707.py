# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-12 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20180812_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
