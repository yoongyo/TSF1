from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.name

SEX = (
    ('Man', 'Man'),
    ('Woman', 'Woman'),
    ('Other','Other'),
)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(blank=True)
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(r'^010[1-9]\d{7}$')], blank=True)
    birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True)
    emergency = models.CharField(max_length=20 ,validators=[RegexValidator(r'^010[1-9]\d{7}$')], blank=True)
    kakaoID = models.CharField(max_length=20, blank=True)
    introduce = models.CharField(max_length=600, blank=True)
    language = models.ForeignKey(Language, blank=True, null=True, on_delete=models.CASCADE)
    major = models.CharField(max_length=20, blank=True, null=True)
    visitedCountry = models.ManyToManyField(Country, related_name='Visited', blank=True, null=True)
    nextCountry = models.ManyToManyField(Country, related_name='Next', blank=True, null=True)
    interest = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=SEX, blank=True, null=True)
    video = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        # 가입시기
        user = kwargs['instance']
        Profile.objects.create(user=user)

        # 환영 이메일 보내기
        send_mail(
            '환영합니다.',
            'here  is th message',
            'jyg0172@naver.com',
            [user.email],
            fail_silently=False,
        )
post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)