# 3. serializer는 DB를 json으로 바꿀 때 사용되며, 반대로 json을 DB로 바꿀 때는 deserializer가 사용된다

from rest_framework import serializers
from rest_framework.renderers import JSONRednerer
from . import models 
import datetime
# 인스턴스 생성 예제
#  article(인스턴스?) = (모델)Article(title="hellow world", content="big world") => article.save()

# user1 = User(nickname='Seoyoon',user_id='qwerty123'...) 후 user1.save() 

