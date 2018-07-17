from django.db import models

class Nationality(models.Model):
    name = models.CharField(max_length=20)

class SNS(models.Model):
    name = models.CharField(max_length=20)

class Language(models.Model):
    name = models.CharField(max_length=20)

class Booking(models.Model):
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Email = models.EmailField(max_length=30)
    Date = models.DateField()
    SNS = models.ForeignKey(SNS)
    Nationality = models.ForeignKey(Nationality)
    phone = models.CharField(max_length=15)
    ConfirmedEmail = models.EmailField(max_length=30)
    Language = models.ForeignKey(Language)