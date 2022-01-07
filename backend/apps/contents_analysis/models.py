from django.db import models
from apps.user.models import User,PreferOttContentGenre

# Create your models here.


# (User와 연관) 1. 하늘 님과 비슷한(연령대) 사람들의 이용시간대(남,녀)
# (6:00~8:59 9:00~11:59 12:00~14:59 15:00~17:59 18:00~20:59 21:00~23:59 24:00~5:59 이용하지않음)
# -> 총 8개 시간대칼럼
# -> 가능하면 전체연령 보여주는거 말고 _0대만 보여주기

class WatchTimeByGender(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(default='하늘')
    gender = models.Integer(default=1)
    age = models.CharField(default='20대')
    time_6_8 = models.IntegerField(default=4.5)
    #

# (X) 2. 최근 소극장에 가장 많이 등록된 장르들(워드클라우드)
# -> 이건 그냥 피그마에 있는 genre_wordcloud.png 로 보내줘도 될 거 같음
# views.py
# @api_view('GET')
# def recently_registered_genres(self,response):
#     return response.data

# (User와 연관) 3. 10대,20대,30대,40대..들의 장르 평균 리뷰 점수      ex.) 20대들의 드라마,코미디,액션.. 평균 리뷰점수
# (드라마 코미디 액션 스릴러 로맨스 범죄 모험 애니메이션 판타지 가족)
# (SF 미스터리 공포 다큐멘터리 전기 역사 음악 단편 스포츠 전쟁 뮤지컬 서부) 
# -> 총 22개 장르컬럼
class ReviewScoreByAge(models.Model):
    nickname = models.CharField(default='하늘')
    age = models.CharField(default='10대')      
    # -> 이렇게 해서 하늘님의 나이가 20대면 
    # -> request.GET.get(age)=='20대' 면 ReviewScoreByAge.objects.get(age='20대')을 보내주고
    drama = models.IntegerField(default=4.5)    
    # -> 엽떡님의 나이가 30대면 
    # -> request.GET.get(age)=='30대' 면 ReviewScoreByAge.objects.get(age='30대')을 보내주고
    comedy = models.IntegerField(default=4.5)
    action = models.IntegerField(default=4.5)
    thriller = models.IntegerField(default=4.5)
    crime = models.IntegerField(default=4.5)
    adventure = models.IntegerField(default=4.5)
    animation = models.IntegerField(default=4.5)
    fantasy = models.IntegerField(default=4.5)


# (X) 4. 코로나 전후로 넷플릭스 한국 장르 증감
# (드라마 코미디 액션 스릴러 로맨스 범죄 모험 애니메이션 판타지 가족)
# (SF 미스터리 공포 다큐멘터리 전기 역사 음악 단편 스포츠 전쟁 뮤지컬 서부) 
# -> 총 22개 장르컬럼
class BeforeAfterCOVID(models.Model):
    id= models.CharField()
# -> 아 이것도 그냥 png로 보내도 될듯
# views.py
#api_view('GET')
#def recently_registered_genres(self,response):
#    return response.data

# (User와 연관) 5,6,7 합쳐서 한 Class로
# 5. 하늘님의 TOP3 중 1번째(액션)를 주로 좋아하는 사람들    
# (남 여 10대 20대 30대 40대 50대 이상) 
# -> 총 7개 컬럼

# 6. 하늘님의 TOP3 중 2번째(로맨스)를 주로 좋아하는 사람들
# (남 여 10대 20대 30대 40대 50대 이상) 
# -> 총 7개 컬럼

# 7. 하늘님의 TOP3 중 3번째(코미디)를 주로 좋아하는 사람들
# (남 여 10대 20대 30대 40대 50대 이상) 
# -> 총 7개 컬럼
class SimilarPeopleScoreTop3(models.Model):
    nickname = models.CharField(default='하늘')
    # -> 이렇게 해서 하늘님의 나이가 20대면 
     # -> request.GET.get(age)=='20대' 면 ReviewScoreByAge.objects.get(age='20대')을 보내주고
    target_genre = models.CharField(default='액션') 
    male = models.IntegerField(default=4.5)
    female = models.IntegerField(default=4.5)
    age_10th = models.IntegerField(default=4.5)
    age_20th = models.IntegerField(default=4.5)
    age_30th = models.IntegerField(default=4.5)
    age_40th = models.IntegerField(default=4.5)
    age_50th = models.IntegerField(default=4.5)

from datetime import datetime
from django.utils import timezone

# 상속 구조 : models.Model -> AbstractBaseUser -> AbstractUser -> User

# Create your models here.
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


# class Prefer_ott_content_genre(models.Model):
#     prefer_genre_1=models.CharField(max_length=50)
#     prefer_genre_2=models.CharField(max_length=50)
#     prefer_genre_3=models.CharField(max_length=50)
#     prefer_genre_4=models.CharField(max_length=50)
#     prefer_genre_5=models.CharField(max_length=50)
#     prefer_genre_6=models.CharField(max_length=50)
#     prefer_genre_7=models.CharField(max_length=50)
#     prefer_genre_8=models.CharField(max_length=50)

# __str__: 이 인스턴스를 조회할 때 보여지는 이름을 정의합니다. 정의하지 않으면 '<Queryset1>' 처럼 안이쁘게 보여지므로 보통 설정하는 편입니다.
# class Meta: 데이터베이스에 담길 시 저장되는 이름을 정의합니다. 정의하지 않으면 '앱이름.클래스이름(user.User)'으로 저장됩니다.

# 이미 장고에서 잘 구현한 User를 OneToOneField(FK와 유사하게 테이블 사용)하고, 내가 필요한 컬럼을 추가로
# 등록하는 확장 방법과
# User가 상속받아 구현한 AbstractUser를 인자로 받아 내가 직접 custom해서 구현하는 방법 2가지 중에 고민하였는데,
# 우리는 장고의 기본 인증 시스템을 재사용 하는게 아니라, 인증 시스템을 jwt를 이용해 구현할 것이기때문에
# AbstractBaseUser를 상속받아 구현한다.

