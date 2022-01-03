from django.db import models

# Create your models here.
class User(models.Model):
    nickname=models.CharField(max_length=50)
    user_id=models.CharField(max_length=50)
    pw=models.TextField(max_length=500)
    birthday=models.DateField(null=True, blank=True) # 날짜만
    gender=models.CharField(max_length=2,null=True, blank=True)
    watch_time=models.TimeField(null=True, blank=True) # 시간대만
    job=models.CharField(max_length=50,null=True, blank=True)
    region=models.CharField(max_length=50,null=True, blank=True)
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

# on_delete : Django에서 모델을 구현할 때 데이터베이스 상에서 참조무결성1을 유지하여 ForeignKeyField가 바라보는 값이 삭제될 때 해당 요소를 처리하는 방법을 지정해 준다.

# CASCADE : ForeignKeyField를 포함하는 모델 인스턴스(row)도 같이 삭제한다. SQL에 상응하는 내용 : CASCADE.
# class Small_theater_group(models.Model):
#     user=models.ForeignKey(User,related_name="small_theater_group", on_delete=models.CASCADE)
#     # theater_owner = user.nickname이랑 어떻게 연관시킬 건지?
#     title = models.CharField(max_length=50)
#     genre_1 = models.CharField(max_length=50)
#     genre_2 = models.CharField(max_length=50)
#     introduce = 
#     published_date = models.DateField(null=True, blank=True)
#     notice = 
