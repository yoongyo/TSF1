# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-11 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', models.CharField(max_length=20)),
                ('FirstName', models.CharField(max_length=20)),
                ('Age', models.PositiveIntegerField()),
                ('gender', models.CharField(blank=True, choices=[('Man', 'Man'), ('Woman', 'Woman'), ('Ohter', 'Other')], max_length=10, null=True)),
                ('Email', models.EmailField(max_length=30)),
                ('Date', models.DateField()),
                ('SNSID', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('ConfirmedEmail', models.EmailField(max_length=30)),
                ('Demand', models.CharField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SNS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='Language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.Language'),
        ),
        migrations.AddField(
            model_name='booking',
            name='Nationality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_nationality', to='accounts.Country'),
        ),
        migrations.AddField(
            model_name='booking',
            name='SNS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.SNS'),
        ),
    ]
