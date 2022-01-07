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
from apps.user.models import User
# Create your models here.

# 1. 하늘 님과 비슷한(연령대) 사람들의 이용시간대(남,녀)
# (6:00~8:59 9:00~11:59 12:00~14:59 15:00~17:59 18:00~20:59 21:00~23:59 24:00~5:59 이용하지않음)
# -> 총 8개 시간대칼럼
# -> png 사용

# 2. 최근 소극장에 가장 많이 등록된 장르들(워드클라우드)
# -> png 사용

# 3. 10대,20대,30대,40대..들의 장르 평균 리뷰 점수      ex.) 20대들의 드라마,코미디,액션.. 평균 리뷰점수
# (드라마 코미디 액션 스릴러 로맨스 범죄 모험 애니메이션 판타지 가족)
# (SF 미스터리 공포 다큐멘터리 전기 역사 음악 단편 스포츠 전쟁 뮤지컬 서부) 
# -> 총 22개 장르컬럼

class ReviewScore(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # nickname = models.CharField(default='하늘')
    # age = models.CharField(default='10대')      # -> 이렇게 해서 하늘님의 나이가 20대면 
                                                 # -> request.GET.get(age)=='20대' 면 ReviewScoreByAge.objects.get(age='20대')을 보내주고
    review_genre = models.CharField(max_length=20, null=True, default='') #드라마
    average_male = models.FloatField(default=0.01) #8.48
    average_female = models.FloatField(default=0.01)
    average_10s = models.FloatField(default=0.01)
    average_20s = models.FloatField(default=0.01)
    average_30s = models.FloatField(default=0.01)
    average_40s = models.FloatField(default=0.01)
    average_50_up = models.FloatField(default=0.01)


# 4. 코로나 전후로 넷플릭스 한국 장르 증감
# (드라마 코미디 액션 스릴러 로맨스 범죄 모험 애니메이션 판타지 가족)
# (SF 미스터리 공포 다큐멘터리 전기 역사 음악 단편 스포츠 전쟁 뮤지컬 서부) 
# -> 총 22개 장르컬럼
# png 사용


# 5,6,7 합쳐서 한 Class로
# 5. 하늘님의 TOP3 중 1번째(액션)를 주로 좋아하는 사람들    
# (남 여 10대 20대 30대 40대 50대 이상) 
# -> 총 7개 컬럼

# 6. 하늘님의 TOP3 중 2번째(로맨스)를 주로 좋아하는 사람들
# (남 여 10대 20대 30대 40대 50대 이상) 
# -> 총 7개 컬럼

# 7. 하늘님의 TOP3 중 3번째(코미디)를 주로 좋아하는 사람들
# (남 여 10대 20대 30대 40대 50대 이상) 
# -> 총 7개 컬럼 

