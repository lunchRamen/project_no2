from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class User(models.Model):
    nickname=models.CharField(max_length=50)
    user_id=models.CharField(max_length=50)
    pw=models.TextField(max_length=500)
    birthday=models.DateField(nullable=True, blank=True)
    gender=models.CharField(max_length=2,nullable=True, blank=True)
    watch_time=models.TimeField(nullable=True, blank=True)
    job=models.CharField(max_length=50,nullable=True, blank=True)
    region=models.CharField(max_length=50,nullable=True, blank=True)
    #small_theater_group=models.CharField(max_length=50)


class Prefer_ott_content_genre(models.Model):
    user=models.ForeignKey(User, related_name="prefer_ott_content",on_delete=models.CASCADE)
    prefer_genre_1=models.CharField(max_length=50)
    prefer_genre_2=models.CharField(max_length=50)
    prefer_genre_3=models.CharField(max_length=50)
    prefer_genre_4=models.CharField(max_length=50)
    prefer_genre_5=models.CharField(max_length=50)
    prefer_genre_6=models.CharField(max_length=50)
    prefer_genre_7=models.CharField(max_length=50)
    prefer_genre_8=models.CharField(max_length=50)