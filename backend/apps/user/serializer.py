from rest_framework import serializers
from .models import User,PreferOttContentGenre
from django.contrib.auth import authenticate

class PreferOttContentGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=PreferOttContentGenre
        fields='__all__'

    def create(self,validated_data):
        prefer_ott_content_genre=PreferOttContentGenre.objects.create(
            **validated_data
            )
        return prefer_ott_content_genre

#회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    
    #1명의 유저 =1개의 선호장르 row. 나중에 된다면 수정도 구현할거니까 read_only False로 설정.
    class Meta:
        model= User
        # exclude=[
        #     'last_login',
        #     'is_active',
        #     'is_admin',
        #     'is_staff',
        #     ]
        fields=[
            'username',
            'password',
            'nickname',
            'birthday',
            'gender',
            'job',
            'region',
            'watch_time',
        ]
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validated_data):
        #username=validated_data['username']
        #password=validated_data['password']
        #prefer_ott_content_genre=validated_data['prefer_ott_content_genre']
        user=User.objects.create_user(
            #username=username,
            **validated_data
        )
        
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


