from rest_framework import serializers
from .models import User,PreferOttContentGenre
from django.contrib.auth import authenticate

#회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        exclude=[
            'last_login',
            'is_active',
            'is_admin',
            'is_staff',
            ]
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validated_data):
        #username=validated_data['username']
        #password=validated_data['password']
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


