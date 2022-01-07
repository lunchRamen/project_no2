from django.db import models
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

