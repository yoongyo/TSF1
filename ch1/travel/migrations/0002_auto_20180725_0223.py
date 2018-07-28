# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-24 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', models.CharField(max_length=20)),
                ('FirstName', models.CharField(max_length=20)),
                ('Age', models.PositiveIntegerField()),
                ('gender', models.CharField(blank=True, choices=[('Man', 'Man'), ('Woman', 'Woman')], max_length=10, null=True)),
                ('Email', models.EmailField(max_length=30)),
                ('Date', models.DateField()),
                ('SNSID', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('ConfirmedEmail', models.EmailField(max_length=30)),
                ('Demand', models.CharField(max_length=1200)),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Language')),
                ('Nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Country')),
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
            model_name='post',
            name='BriefCourse',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='DurationCourse',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Photography',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='SeasonFrom',
            field=models.DateField(default='2012-12-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='SeasonTo',
            field=models.DateField(default='2012-12-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='SNS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.SNS'),
        ),
        migrations.AddField(
            model_name='post',
            name='booking',
            field=models.ManyToManyField(to='travel.Booking'),
        ),
    ]