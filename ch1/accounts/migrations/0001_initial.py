from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^010[1-9]\\d{7}$')])),
                ('birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('emergency', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^010[1-9]\\d{7}$')])),
                ('kakaoID', models.CharField(blank=True, max_length=20)),
                ('introduce', models.CharField(blank=True, max_length=600)),
                ('major', models.CharField(blank=True, max_length=20, null=True)),
                ('interest', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Man', 'Man'), ('Woman', 'Woman'), ('Other', 'Other')], max_length=10, null=True)),
                ('video', models.URLField(blank=True, null=True)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Language')),
                ('nextCountry', models.ManyToManyField(blank=True, null=True, related_name='Next', to='accounts.Country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visitedCountry', models.ManyToManyField(blank=True, null=True, related_name='Visited', to='accounts.Country')),
            ],
        ),
    ]