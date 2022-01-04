from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from .validators import NickNameValidator

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


#django의 기본 그룹, 허가권 관리를 해줘야하는지 잘 모르겠지만,
#일단 해봄.
#,null=True, blank=True

#버전1에서 배열을 db에 어떤 형태로 집어넣어 줘야할지,생각이 안나고
#만약에 풀어 쓴다고해도 다시 genre_list테이블을 만들어서
#거기에 집어넣어준 다음에 OneToOneField를 해줘야 할거같다 버전2채택.
class PreferOttContentGenre(models.Model):
    #id=models.AutoField(primary_key=True)

    title=models.CharField(max_length=100,null=True, blank=True)

    drama=models.IntegerField(null=True, blank=True)
    comedy=models.IntegerField(null=True, blank=True)
    action=models.IntegerField(null=True, blank=True)
    thriller=models.IntegerField(null=True, blank=True)
    romance=models.IntegerField(null=True, blank=True)
    crime=models.IntegerField(null=True,blank=True)
    adventure=models.IntegerField(null=True, blank=True)
    animation=models.IntegerField(null=True, blank=True)
    fantasy=models.IntegerField(null=True, blank=True)
    family=models.IntegerField(null=True, blank=True)
    sci_fi=models.IntegerField(null=True, blank=True)
    mystery=models.IntegerField(null=True, blank=True)
    horror=models.IntegerField(null=True, blank=True)
    document=models.IntegerField(null=True, blank=True)
    biography=models.IntegerField(null=True, blank=True)
    history=models.IntegerField(null=True, blank=True)
    music=models.IntegerField(null=True,blank=True)
    short=models.IntegerField(null=True, blank=True)
    sport=models.IntegerField(null=True, blank=True)
    war=models.IntegerField(null=True, blank=True)
    musical=models.IntegerField(null=True, blank=True)
    reality_tv=models.IntegerField(null=True, blank=True)
    western=models.IntegerField(null=True, blank=True)
    game_show=models.IntegerField(null=True, blank=True)
    talk_show=models.IntegerField(null=True, blank=True)

    img_link=models.CharField(max_length=256,null=True, blank=True)


class UserManager(BaseUserManager):
    def create_user(self,username,password,**extra_kwargs):
        if not username:
            raise ValueError('id를 입력하지 않았습니다.')
        user= self.model(
            username=username,
            **extra_kwargs
        )
        user.set_password(password)
        user.save(self._db)
        return user
        
    def create_superuser(self, username,password,**extra_kwargs):
        extra_kwargs.setdefault('is_admin',True)
        extra_kwargs.setdefault('is_superuser',True)
        extra_kwargs.setdefault('is_staff',True)
        user= self.create_user(username,password,**extra_kwargs)
        #user.is_admin=True
        #user.is_superuser=True
        user.save(self._db)
        return user
        


class User(AbstractBaseUser,PermissionsMixin):
    class Meta:
        db_table='user'

    #id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True)
    
    nickname_validator=NickNameValidator()
    nickname=models.CharField(
        max_length=50,
        validators=[nickname_validator]
    )

    birthday=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=50,null=True, blank=True)
    job=models.CharField(max_length=50,null=True, blank=True)
    region=models.CharField(max_length=50,null=True, blank=True)
    watch_time=models.IntegerField(null=True, blank=True)

    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    prefer_ott_content_genre=models.OneToOneField(PreferOttContentGenre,on_delete=models.CASCADE,null=True, blank=True)

    object=UserManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.nickname





