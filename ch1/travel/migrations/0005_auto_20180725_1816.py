# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-25 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_merge_20180725_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='booking',
        ),
        migrations.AddField(
            model_name='booking',
            name='content',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='travel.Post'),
            preserve_default=False,
        ),
    ]