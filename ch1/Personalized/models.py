from django.db import models
from django.conf import settings
import sys
sys.path.append('..')
from travel.models import SNS, TypeOfTour, City, Language, Time, Duration
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django import forms
import sys
sys.path.append('..')
from accounts.models import Country
import re

SEX = (
    ('Man', 'Man'),
    ('Woman', 'Woman'),
    ('Other', 'Other'),
)

def password(value):
    p = re.compile(r'^[0-9]+$')
    m = p.match(value)
    if m:
        pass
    else:
        raise forms.ValidationError('only number')


class Personalized(models.Model):
    # tour type
    title = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10, choices=SEX)
    City = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=4, validators=[RegexValidator(r'^[0-9]+$', "only number")])
    Date = models.CharField(max_length=100)
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

class PersonalizedTour(models.Model):
    content = models.OneToOneField(Personalized, null=True, blank=True, unique=True, related_name="personalized")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    # Basic Information
    title = models.CharField(max_length=30)
    Tourtype = models.ForeignKey(TypeOfTour, on_delete=models.CASCADE)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='Personalized_country')
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    DetailContent = models.CharField(max_length=1200,
                                     help_text='당신이 만든 local 여행에 대한 설명을 자유롭게 작성해 주세요.<br>Tip. 당신의 Tour만이 가지고 있는 특징에 대해 설명해주세요. 외국인은 언제나 local다움과 funny한 상품을 찾고 있습니다.')
    BriefContent = models.TextField(max_length=250)
    HashTag = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True)

    # Course Information
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
    GuestInfo = models.CharField(max_length=100)

    # etc
    Created_at = models.DateTimeField(auto_now_add=True)

    # 심사
    confirm = models.NullBooleanField(null=True, blank=True)

    SeasonFrom = models.DateField()
    SeasonTo = models.DateField()

    def __str__(self):
        return str(self.content)

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


