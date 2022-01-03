from django.db import models
from datetime import datetime
from django.utils import timezone

# 상속 구조 : models.Model -> AbstractBaseUser -> AbstractUser -> User

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from .validators import UserNameValidator

class Prefer_ott_content_genre(models.Model):
    prefer_genre_1=models.CharField(max_length=50)
    prefer_genre_2=models.CharField(max_length=50)
    prefer_genre_3=models.CharField(max_length=50)
    prefer_genre_4=models.CharField(max_length=50)
    prefer_genre_5=models.CharField(max_length=50)
    prefer_genre_6=models.CharField(max_length=50)
    prefer_genre_7=models.CharField(max_length=50)
    prefer_genre_8=models.CharField(max_length=50)

# __str__: 이 인스턴스를 조회할 때 보여지는 이름을 정의합니다. 정의하지 않으면 '<Queryset1>' 처럼 안이쁘게 보여지므로 보통 설정하는 편입니다.
# class Meta: 데이터베이스에 담길 시 저장되는 이름을 정의합니다. 정의하지 않으면 '앱이름.클래스이름(user.User)'으로 저장됩니다.

# 이미 장고에서 잘 구현한 User를 OneToOneField(FK와 유사하게 테이블 사용)하고, 내가 필요한 컬럼을 추가로
# 등록하는 확장 방법과
# User가 상속받아 구현한 AbstractUser를 인자로 받아 내가 직접 custom해서 구현하는 방법 2가지 중에 고민하였는데,
# 우리는 장고의 기본 인증 시스템을 재사용 하는게 아니라, 인증 시스템을 jwt를 이용해 구현할 것이기때문에
# AbstractBaseUser를 상속받아 구현한다.

