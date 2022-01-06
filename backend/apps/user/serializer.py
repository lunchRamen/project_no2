from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from .models import User,PreferOttContentGenre
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

class PreferOttContentGenreSerializer(serializers.ListSerializer):
    class Meta:
        model=PreferOttContentGenre
        fields='__all__'


#회원가입
class CreateUserSerializer(serializers.ModelSerializer):

    #prefer_ott_content_genre_serializer = PreferOttContentGenreSerializer()
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
        
#    def validate_username(self,data):
#        #User테이블에서 입력받은 username(id)값과 같은게 있는지 가져와봄.
#        user=User.objects.filter(username=data['username'])

        #만약 user가 있다면

#        if user:
#            raise serializers.ValidationError('해당 아이디가 이미 존재합니다.')

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


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
#로그인
class LoginUserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=128,write_only=True)
    token=serializers.CharField(max_length=255,read_only=True)


    def validate(self,data):
        username=data.get('username',None)
        password=data.get('password',None)
        user=authenticate(username=username,password=password)

        if user is None:
           raise serializers.ValidationError('해당 아이디는 없는 아이디입니다.')

        try:
            payload=JWT_PAYLOAD_HANDLER(user)
            jwt_token=JWT_ENCODE_HANDLER(payload)
            update_last_login(None,user)

        except User.DoesNotExist:
            raise serializers.ValidationError("아이디나 비밀번호가 맞지 않습니다.")

        login_serialize={
            'username':user.username,
            'token':jwt_token,
        }
        return login_serialize

