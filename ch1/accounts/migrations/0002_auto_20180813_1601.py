# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='image',
            field=models.ImageField(upload_to='Country/'),
        ),
    ]