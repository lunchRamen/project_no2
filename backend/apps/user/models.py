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


class UserManager(BaseUserManager): # UserManager 쓰는 이유 : create_user를 쓰기 위해
    def create_user(self, user_id, password, **extra_fields):
        user = self.model(
            user_id=user_id,
            password=password,
        )
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        user.set_password(password) # set_password: 회원가입시 받은 비밀번호를 hash하여 저장하는 함수
        user.save(using=self._db)
        return user

def create_superuser(self, user_id,password,**extra_fields):
        user=self.model(
            user_id=user_id,
            password=password,
            **extra_fields
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    username_validator =UserNameValidator()
    nickname=models.CharField(
        verbose_name='닉네임',
        max_length=50,
        unique=True,
        validators=[username_validator]
    )
    user_id=models.CharField(max_length=50,unique=True)
    # pw=models.TextField(max_length=500) AbstractBaseUser에 이미 있는 컬럼.

    birthday=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=2,null=True, blank=True)
    watch_time=models.IntegerField(null=True, blank=True)#time을 그냥 시간대말고 우리끼리 정의한
    #value 0이면 00:00~03:00 1이면 03:00~06:00 ... 이렇게 정의하는걸로 하자.

    job=models.CharField(max_length=50,null=True, blank=True)
    region=models.CharField(max_length=50,null=True, blank=True)
    #small_theater_group=models.CharField(max_length=50) 일단 보류.
    prefer_ott_content_genre=models.OneToOneField(Prefer_ott_content_genre,on_delete=models.CASCADE)

    #AbstractBaseUser상속으로 만들어줘야하는 필드.
    is_staff=models.BooleanField(default=False) #우린 관리자(사장님페이지)가 없으므로 0으로 고정
    is_active=models.BooleanField(default=True) #is_active는 현재 해당 유저 계정이 활성화 되었는지 1으로 고정

    objects=UserManager()

    USERNAME_FIELD='user_id'
    REQUIRED_FIELDS=[]

    class Meta:
        db_table='user'

    def __str__(self):
        return self.nickname
