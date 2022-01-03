# serializer : 객체처럼 보기힘든 데이터를 JSON이나 XML으로 보기쉽게 데이터 바꿔줌
# REST API : Resource 이름가지고 클라이언트와 서버가 통신하는 방법 만들 때 필수적임

# 주의! 장고 서버와 REST 서버는 따로 운영되어야 한다!!
from .models import SmallTheater
from rest_framework import serializers

class SmallTheaterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmallTheater # models.py속 모델
        fields = ('no','published_date','title','theater_owner','theater_genre1','theater_genre2','introduce','notice') # 통신할 데이터필드