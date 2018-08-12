from django.db import models
import sys
sys.path.append('..')
from travel.models import Post,Booking
from django.core.validators import MinValueValidator, MaxValueValidator




class Review(models.Model):
    post = models.ForeignKey(Post, related_name='post')
    booking = models.OneToOneField(Booking, related_name='booking')
    review1 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review2 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review3 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review4 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review5 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])