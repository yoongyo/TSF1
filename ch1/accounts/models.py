from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(r'^010[1-9]\d{7}$')])
    birth = models.DateField()
    email = models.EmailField()
    emergency = models.CharField(max_length=20 ,validators=[RegexValidator(r'^010[1-9]\d{7}$')])
    kakaoID = models.CharField(max_length=20)
    introduce = models.CharField(max_length=600)
    language = models.ForeignKey(Language)
    major = models.CharField(max_length=20)
    visitedCountry = models.ForeignKey(Country, related_name='Visited')
    nextCountry = models.ForeignKey(Country, related_name='Next')
    interest = models.CharField(max_length=20)
