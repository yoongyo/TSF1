from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

import sys
sys.path.append('..')
from accounts import models as pd

import sys
sys.path.append('..')
from accounts.models import Country,Profile


class TypeOfTour(models.Model):
    type = models.CharField(max_length=30)
    img = models.ImageField()

    def __str__(self):
        return self.type



class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=15)
    video = models.URLField(blank=True, null=True)
    img = models.ImageField()

    def __str__(self):
        return self.city

class Language(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language

class SNS(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


SEX = (
    ('Man', 'Man'),
    ('Woman', 'Woman'),
    ('Other', 'Other'),
)

class Time(models.Model):
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.time

class Duration(models.Model):
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.duration

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    # Basic Infomation
    title = models.CharField(max_length=30)
    Tourtype = models.ForeignKey(TypeOfTour, on_delete=models.CASCADE)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='travel_country')
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    DetailContent = models.CharField(max_length=1200, help_text='당신이 만든 local 여행에 대한 설명을 자유롭게 작성해 주세요.<br>Tip. 당신의 Tour만이 가지고 있는 특징에 대해 설명해주세요. 외국인은 언제나 local다움과 funny한 상품을 찾고 있습니다.')
    BriefContent = models.TextField(max_length=250)
    HashTag = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True, upload_to='photos/')

    # Course Infomation
    MeetingPoint = models.CharField(max_length=130)
    MeetingTime = models.ForeignKey(Time)
    Map = models.CharField(max_length=140)
    Direction = models.CharField(max_length=200)


    Duration = models.ForeignKey(Duration)

    # Price & Other Information
    Price = models.CharField(max_length=10)
    Minimum = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    Maximum = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    Price_include = models.CharField(max_length=100)

    # 달력 구현원함
    NotDate = models.TextField(blank=True)
    GuestInfo = models.CharField(max_length=1000)

    # etc
    Created_at = models.DateTimeField(auto_now_add=True)

    # 대표 포스팅
    representation = models.NullBooleanField(blank=True, null=True)

    # 심사
    confirm = models.NullBooleanField(null=True, blank=True)

    SeasonFrom = models.DateField()
    SeasonTo = models.DateField()



    def __str__(self):
        return self.title

    @property
    def lng(self):
        if self.Map:
            return self.Map.split(',')[1]
        return None

    @property
    def lat(self):
        if self.Map:
            return self.Map.split(',')[0]
        return None


    # def get_absolute_url(self):
        # return reverse('travel:local_detail_form', args=[self.City, self.name])



class Booking(models.Model):
    content = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    Age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=SEX, blank=True, null=True)
    Email = models.EmailField(max_length=30)
    Date = models.DateField()
    SNS = models.ForeignKey(SNS, on_delete=models.CASCADE)
    SNSID = models.CharField(max_length=20)
    Nationality = models.ForeignKey(Country)
    phone = models.CharField(max_length=15)
    ConfirmedEmail = models.EmailField(max_length=30)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    Demand = models.CharField(max_length=1200)
    NOP = models.PositiveIntegerField()

    def __str__(self):
        return self.FirstName

    def get_absolute_url(self):
        return reverse('travel:bookingcomplete', args=[self.content__City, self.content_pk])




















