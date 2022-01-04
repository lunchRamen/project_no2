from django.http import response #안씀
from django.shortcuts import render #안씀
from django.views import generic #안씀
from rest_framework.views import APIView #CBV
from rest_framework import status #200 404 등
from rest_framework.response import Response
# from rest_framework.decorators import api_view # @api_view FBV
from .models import SmallTheater
from .serializers import SmallTheaterSerializer
# FBV와 Generic View가 있음
# FBV는 세세하게 코딩/ Generic view는 간편 -> 섞어도 됨

# POST,GET 둘다 요청 
# POST은 뭔가 sideeffect가 있을 때(바뀌거나 넣어줘야 할 때) GET은 응답(데이터)만 주면 될 때

# CBV POST,GET,DELETE,UPDATE 참고사이트 
# https://toughbear.tistory.com/60
# **kwargs https://d-yong.tistory.com/61
# 공식문서 https://www.django-rest-framework.org/tutorial/3-class-based-views/

# static, 템플릿 등 참고사이트 https://iamiet.tistory.com/10?category=928115
# api 요청 이용해 drf <-> 리엑트 연동 https://this-programmer.tistory.com/135
# 쿼리셋 검색방법 https://velog.io/@swhybein/django-queryset
# Create your views here.

class SmallTheaterList(APIView): # 소극장 전체 또는 일부 보기
    def get(self,request,**kwargs): # http://localhost/small-theater?theater_genre1=romance&theater_genre2=romance&theater_genre1=drama&theater_genre2=drama&title=마블
        small_theater_list = SmallTheater.objects.all() #쿼리에 따라 DB에 있는 소극장 목록 가져오기
        small_theater_serializer = SmallTheaterSerializer(small_theater_list)
        return Response(small_theater_serializer.data,status=status.HTTP_200_OK)

class SmallTheaterDetail(APIView): # 소극장 상세보기
    def get(self,request,**kwargs): #http://localhost:8000/small-theater{small_theater.id}
        target_theater_id = kwargs.get('id') 
        queryset = SmallTheater.objects.get(id=target_theater_id)
        target_theater_serializer = SmallTheaterSerializer(queryset)
        return Response(target_theater_serializer.data, status=status.HTTP_200_OK)