# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personalized', '0004_auto_20180813_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalizedtour',
            name='City',
            field=models.CharField(max_length=50),
        ),
    ]
