# 3. serializer는 DB를 json으로 바꿀 때 사용되며, 반대로 json을 DB로 바꿀 때는 deserializer가 사용된다

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from . import models 
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# 인스턴스 생성 예제
#  article(인스턴스?) = (모델)Article(title="hellow world", content="big world") => article.save()

# user1 = User(nickname='Seoyoon',user_id='qwerty123'...) 후 user1.save() 

#회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model='User'
        fields =('id','user_id','nickname','password')
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validated_data):
        user=User.objects.create_user(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user

#접속 유지 확인용
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username')

#로그인
class LoginUserSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        user=authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("존재하지 않는 회원입니다.")
