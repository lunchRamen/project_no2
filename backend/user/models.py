from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager,User

"""
이미 장고에서 잘 구현한 User를 OneToOneField(FK와 유사하게 테이블 사용)하고, 내가 필요한 컬럼을 추가로
등록하는 확장 방법과
User가 상속받아 구현한 AbstractUser를 인자로 받아 내가 직접 custom해서 구현하는 방법 2가지 중에 고민하였는데,
커스텀 가능한 후자로 진행하기로!


model의 상속 구조는
models.Model -> AbstractBaseUser -> AbstractUser -> User 순으로 상속이 되어있다.

"""
class User(AbstractBaseUser,PermissionsMixin):
    nickname=models.CharField(max_length=50)
    user_id=models.CharField(max_length=50,unique=True)
    pw=models.TextField(max_length=500)
    birthday=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=2,null=True, blank=True)
    watch_time=models.TimeField(null=True, blank=True)
    job=models.CharField(max_length=50,null=True, blank=True)
    region=models.CharField(max_length=50,null=True, blank=True)
    #small_theater_group=models.CharField(max_length=50)
    objects=UserManager()

    USERNAME_FIELD='user_id'







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