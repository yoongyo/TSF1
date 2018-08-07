from django.db import models
import sys
sys.path.append('..')
from travel.models import SNS

import sys
sys.path.append('..')
from accounts.models import Country

SEX = (
    ('Man', 'Man'),
    ('Woman', 'Woman'),
)


class Personalized(models.Model):
    title = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10, choices=SEX)
    City = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=4)
    Date = models.DateField()
    SNS = models.ForeignKey(SNS)
    Language = models.CharField(max_length=20)
    Cellnumber = models.CharField(max_length=20, blank=True, null=True)
    SNSID = models.CharField(max_length=15)
    Content = models.TextField()
    Price = models.CharField(max_length=15)
    Guest = models.PositiveIntegerField()
    Nationality = models.ForeignKey(Country)

    def __str__(self):
        return self.title