# 3. serializer는 DB를 json으로 바꿀 때 사용되며, 반대로 json을 DB로 바꿀 때는 deserializer가 사용된다

from rest_framework import serializers
from rest_framework.renderers import JSONRednerer
from . import models 
import datetime
# 인스턴스 생성 예제
#  article(인스턴스?) = (모델)Article(title="hellow world", content="big world") => article.save()

# user1 = User(nickname='Seoyoon',user_id='qwerty123'...) 후 user1.save() 
class UserSerializer(serializers.Serializer):
    nickname = serializers.CharField()
    user_id=serializers.CharField()
    pw=serializers.TextField()
    birthday=serializers.DateField() # 날짜만
    gender=serializers.CharField()
    watch_time=serializers.TimeField() # 시간대만
    job=serializers.CharField()
    region=serializers.CharField()
    def create(self, validated_data) :
        return models.User.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        ....

# serializer
serializer = UserSerializer(models.User)
print(serializer) #딕셔너리
serializer_json = JSONRenderer().render(serializer.data) #JSON 형태

# deserializer
import io
from rest_framework.parsers import JSONParser
stream = io.BytesIO(serializer_json)
data = JSONParser().parse(stream)

# serializer. save()를 통해 호출할 때 인스턴스의 생성이나 수정이 이루어지는데, 어떻게 로직이 이루어지는지를 정하기 위해 create()와 update()를 사용한다. 
#인스턴스 생성
user1 = models.User(nickname='seoyoon',user_id='qwert123',pw='1234',birthday='99-04-27',gender='female',watch_time=datetime.time(16,00,30),job='student',region='seoul')
# 인스턴스 하나 DB에 저장
user1.save()

# 인자1개 = create로직
serializer2 = UserSerializer(data = data) 
# 모든 칼럼을 다 넣어야 하지만, required=False를 넣으면 일부 칼럼에 None이 포함되더라도 error가 발생하지 않는다.
serializer_required = UserSerializer(required=False)
# 기본적으로 serializer는 모든 필수 필드의 값을 전달해야 합니다. 그렇지 않으면 유효성 검사 오류가 발생합니다. 그러나 수정 상황에서는 무든 필수 필드를 넣을 필요 없이 수정할 필드만 넣어주면 된다. 그때 사용하는 것이 partial=True이다. 아래와 같이 사용하면 된다.
user2 = UserSerializer(user1, data = {'nickname'='hi'....}, partial=True)
#인자2개 = update로직(DB값 수정) 
serializer3 = UserSerializer(user1, data=data) 
serializer2.is_valid() # True
# deserializer을 하여 데이터에 접근하거나 DB에 저장할 때는 반드시 is_valid()를 호출해서 확인을 해줘야 한다
serializer2.validated_data # 다시 딕셔너리로 
