# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0018_auto_20180801_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='representation',
            field=models.NullBooleanField(),
        ),
    ]
