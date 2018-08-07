# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-06 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_auto_20180723_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Nationality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_nationality', to='accounts.Country'),
        ),
        migrations.DeleteModel(
            name='Nationality',
        ),
    ]
