from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,User
from .validators import UserNameValidator

"""
이미 장고에서 잘 구현한 User를 OneToOneField(FK와 유사하게 테이블 사용)하고, 내가 필요한 컬럼을 추가로
등록하는 확장 방법과
User가 상속받아 구현한 AbstractUser를 인자로 받아 내가 직접 custom해서 구현하는 방법 2가지 중에 고민하였는데,
우리는 장고의 기본 인증 시스템을 재사용 하는게 아니라, 인증 시스템을 jwt를 이용해 구현할 것이기때문에
AbstractBaseUser를 상속받아 구현한다.

model의 상속 구조는
models.Model -> AbstractBaseUser -> AbstractUser -> User 순으로 상속이 되어있다.

하나의 유저는 하나의 선호장르 선택만 할 수있음(수정을 통해서도 하나의 결과값을 다시 도출)
1:N인 FK보다 OneToOne으로 매핑시켜서 바로 접근 가능하게끔.

unique는 nickname과 user_id 두개를 지정.

그리고 UserManager를 오버라이딩해서 내가 원하는 속성들로 create_user,기타 함수들을 구현하고 싶은데
내가 하는게 맞는건지 잘 모르겠다...

질문1
UserManager를 이렇게 오버라이딩 해도 괜찮은건지..
User의 경우도 오버라이딩을 잘 한게 맞는건지...




"""
class Prefer_ott_content_genre(models.Model):
    prefer_genre_1=models.CharField(max_length=50)
    prefer_genre_2=models.CharField(max_length=50)
    prefer_genre_3=models.CharField(max_length=50)
    prefer_genre_4=models.CharField(max_length=50)
    prefer_genre_5=models.CharField(max_length=50)
    prefer_genre_6=models.CharField(max_length=50)
    prefer_genre_7=models.CharField(max_length=50)
    prefer_genre_8=models.CharField(max_length=50)

class UserManager(BaseUserManager):
    def create_user(self, user_id, password,**extra_fields):
        user=self.model(
            user_id=user_id,
            password=password,
        )
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        user.set_password(password)
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
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects=UserManager()

    USERNAME_FIELD='user_id'
    REQUIRED_FIELDS=[]

    class Meta:
        db_table='user'

    def __str__(self):
        return self.nickname




