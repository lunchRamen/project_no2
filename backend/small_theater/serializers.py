# serializer : 객체처럼 보기힘든 데이터를 JSON이나 XML으로 보기쉽게 데이터 바꿔줌
# REST API : Resource 이름가지고 클라이언트와 서버가 통신하는 방법 만들 때 필수적임

# 주의! 장고 서버와 REST 서버는 따로 운영되어야 한다!!
from rest_framework import serializers
from .models import SmallTheater

# 리엑트연동까지 https://this-programmer.tistory.com/135
# Serializer 자세한 설명 https://brownbears.tistory.com/71
class SmallTheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallTheater # models.py속 모델
        fields = ('__all__') # 통신할 데이터필드 -> 모든 필드 하려면 '__all__'해도 됨
        # fields = ('id','published_date'...,)