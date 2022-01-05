from django.http import response, JsonResponse, HttpResponse #안씀
from django.shortcuts import render #안씀
from django.views import generic #안씀
from django.db.models import Q #filter시 | 사용하려고 
from urllib import parse #한글 인코딩
from rest_framework.views import APIView #CBV
from rest_framework import status,generics #200 404 등 , ListAPIView
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
# 쿼리셋 <-> JSON https://www.delftstack.com/ko/howto/django/django-queryset-to-json/

# static, 템플릿 등 참고사이트 https://iamiet.tistory.com/10?category=928115
# api 요청 이용해 drf <-> 리엑트 연동 https://this-programmer.tistory.com/135
# 쿼리셋 all order_by filter 사용법 https://velog.io/@swhybein/django-queryset
# Create your views here.

# 쿼리셋 filter, ordering 일본개발자 블로그 https://freez2385.github.io/posts/Python-Django-django_restframework2/
# filtering, ordering 블로그2 https://donis-note.medium.com/django-rest-framework-filtering%EA%B3%BC-ordering-4e7d1351205a
# 딕셔너리 .get, .items() 등등 https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sw4r&logNo=221504133335
# 한글인코드 https://dololak.tistory.com/255


# 1.
# class SmallTheaterList(APIView): # 소극장 전체 보기는 구현완료 
#     def get(self,request,**kwargs): # http://localhost/small-theater?search_genre1=romance&search_genre2=romance&title=마블
#         small_theater_list = SmallTheater.objects.all() #쿼리에 따라 DB에 있는 소극장 목록 가져오기
#         small_theater_serializer = SmallTheaterSerializer(small_theater_list,many=True)
#         return Response(small_theater_serializer.data,status=status.HTTP_200_OK)

# 2.
class SmallTheaterList(APIView): # 소극장 목록 보기
    # http://localhost/small-theater?search-genre1=drama&search-genre2=romance&title=마블
    def get(self,request,**kwargs):
        search_genre1 = request.GET.get('search-genre1')
        search_genre2 = request.GET.get('search-genre2')
        search_title =request.GET.get('title')
        for key in request.GET.keys():
            if request.GET.get(key)!=None:
                parse.unquote(request.GET.get(key)) #None이 아니면 한글로 바꿔라
        # 1. genre1,genre2,title 셋 다 None인 경우
        if (search_genre1==None) & (search_genre2==None) & (search_title==None):
            final_queryset = SmallTheater.objects.all().order_by('-published_date') # /small-theater
        # 2. title이 있는 경우(__contains오류 떄문에 얘만 따로)
        elif search_title: 
            queryset = SmallTheater.objects.filter(Q(theater_genre1=search_genre1) | Q(theater_genre2=search_genre1) | Q(theater_genre1=search_genre2) | Q(theater_genre2=search_genre2) | Q(title__contains=search_title)) #단어포함 title__contains = 어쩌구
            final_queryset = queryset.order_by('-published_date') #published_date하면 오름차순
        # 3. genre1,genre2,title 중 하나라도 있는 경우
        else:
            queryset = SmallTheater.objects.filter(Q(theater_genre1=search_genre1) | Q(theater_genre2=search_genre1) | Q(theater_genre1=search_genre2) | Q(theater_genre2=search_genre2) | Q(title=search_title)) #단어포함 title__contains = 어쩌구
            final_queryset = queryset.order_by('-published_date')
        target_theater_serializer = SmallTheaterSerializer(final_queryset, many=True)
        return Response(target_theater_serializer.data, status=status.HTTP_200_OK)
        
class SmallTheaterDetail(APIView): # 소극장 상세보기
    def get(self,request,**kwargs): #http://localhost:8000/small-theater/{small_theater.id}
        target_theater_id = kwargs.get('id') # 4 (int)
        queryset = SmallTheater.objects.filter(id=target_theater_id) # get은 하나만 가져옴 not iterable이슈 있음
        target_theater_serializer = SmallTheaterSerializer(queryset, many=True)
        return Response(target_theater_serializer.data, status=status.HTTP_200_OK)