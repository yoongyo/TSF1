from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

import sys
sys.path.append('..')
from accounts import models as pd



class TypeOfTour(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Country(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=15)

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
)




class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    # Basic Infomation
    title = models.CharField(max_length=30)
    Tourtype = models.ForeignKey(TypeOfTour, on_delete=models.CASCADE)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    DetailContent = models.CharField(max_length=1200, help_text='당신이 만든 local 여행에 대한 설명을 자유롭게 작성해 주세요.<br>Tip. 당신의 Tour만이 가지고 있는 특징에 대해 설명해주세요. 외국인은 언제나 local다움과 funny한 상품을 찾고 있습니다.')
    BriefContent = models.CharField(max_length=250)
    HashTag = models.CharField(max_length=20)
    img = models.ImageField()

    # Course Infomation
    MeetingPoint = models.CharField(max_length=50)
    MeetingTime = models.CharField(max_length=30)
    Map = models.CharField(max_length=10)
    Direction = models.CharField(max_length=200)
    CourseName = models.CharField(max_length=40)
    DurationCourse = models.CharField(max_length=80)
    BriefCourse = models.CharField(max_length=1000)
    Photography = models.ImageField()
    Duration = models.CharField(max_length=20)

    # Price & Other Information
    Price = models.CharField(max_length=10)
    Minimum = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    Maximum = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    Price_include = models.CharField(max_length=100)
    # 달력 구현원함
    NotDate = models.DateField()
    GuestInfo = models.CharField(max_length=100)

    # etc
    Created_at = models.DateTimeField(auto_now_add=True)

    # 대표 포스팅
    representation = models.BooleanField(blank=True)

    # 심사
    confirm = models.BooleanField(blank=True)

    SeasonFrom = models.DateField()
    SeasonTo = models.DateField()



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('travel:local_detail_form', args=[self.City, self.name])


class Booking(models.Model):
    content = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    Age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=10, choices=SEX, blank=True, null=True)
    Email = models.EmailField(max_length=30)
    Date = models.DateField()
    SNS = models.ForeignKey(SNS, on_delete=models.CASCADE)
    SNSID = models.CharField(max_length=20)
    Nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    ConfirmedEmail = models.EmailField(max_length=30)
    Language = models.ForeignKey(Language,on_delete=models.CASCADE)
    Demand = models.CharField(max_length=1200)

    def __str__(self):
        return self.FirstName

    def get_absolute_url(self):
        return reverse('travel:bookingcomplete', args=[self.content__City, self.content_pk])



















