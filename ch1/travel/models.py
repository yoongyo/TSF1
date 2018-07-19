from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings




class TypeOfTour(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Country(models.Model):
    country = models.CharField(max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.country

class City(models.Model):
    country = models.ForeignKey(Country)
    city = models.CharField(max_length=15)

    def __str__(self):
        return self.city

class Language(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language

class Post(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Basic Infomation
    title = models.CharField(max_length=30)
    Tourtype = models.ForeignKey(TypeOfTour)
    Country = models.ForeignKey(Country)
    City = models.ForeignKey(City)
    Language = models.ForeignKey(Language)
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


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('travel:local_detail_form', args=[self.City, self.name])
























