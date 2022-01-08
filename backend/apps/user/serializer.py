from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from .models import User,PreferOttContentGenre
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

class PreferOttContentGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=PreferOttContentGenre
        fields='__all__'


#회원가입
class CreateUserSerializer(serializers.ModelSerializer):

    #prefer_ott_content_genres=serializers.PrimaryKeyRelatedField(many=True,allow_empty=False)
    class Meta:
        model= User
        fields=[
            'username',
            'password',
            'nickname',
            'birthday',
            'gender',
            'watch_time',
            'prefer_ott_content_genres',
        ]
        extra_kwargs={'password':{'write_only':True}}
        #serializer relations. FK나 m2m field가 바뀜. -> pk related table 생성됨.
        

    def create(self,validated_data):
        #고른 선호장르 8개의 id가 list형태로 담겨져서 옴.
        #prefer_ott_content_genres=validated_data['prefer_ott_content_genres']

        #validated_data['prefer_ott_content_genres'] -> pk로 보내면 m2m이 어떻게 저장되는지 먼저 확인.
        #오는 값이 pk로 오는지, 아니면 id에 해당하는 object를 가져 오는지 확인. 유효하면, 가져올때 object로 오는지 id로 오는지 확인.
        #m2m으로 매핑되어있어서 동시에 생성이 된다(에러 안남)
        #마지막으론 m2m필드의 set이나 add를 통하고 save.-> 이건 view단에서.
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
#ModelSerializer로 구현 한번 해보는걸로 하자.
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

