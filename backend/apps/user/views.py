from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .models import User,PreferOttContentGenre

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView,View
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, GenericAPIView,ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from .serializer import CreateUserSerializer, LoginUserSerializer,PreferOttContentGenreSerializer
import csv
import random

"""
View에도 Model처럼 4계층으로 상속이 진행됨.
APIView -> GenericView -> Concrete View classes -> Viewsets
"""
#title,drama,comedy,action,thriller,romance,crime,adventure,animation,fantasy,family,
# sci-fi,mystery,horror,documentary,biography,history,music,short,sport,war,musical,
# reality-tv,western,game-show,talk-show,img_link

#왜 csv.DictReader로 했을때 인식을 못했을까.. 시간이 남을때 이걸로 다시 실행해보자.
# def csvToModel(request):
#     with open('apps/user/ott_contents.csv','r') as f:
#         # rows = csv.reader(f, delimiter = ',')
#         data=f.readline()
#         rows=csv.reader(f,delimiter = ',')
#         for row in rows:
#             PreferOttContentGenre.objects.create(
#                 title=row[0],
#                 drama=row[1],
#                 comedy=row[2],
#                 action=row[3],
#                 thriller=row[4],
#                 romance=row[5],
#                 crime=row[6],
#                 adventure=row[7],
#                 animation=row[8],
#                 fantasy=row[9],
#                 family=row[10],
#                 sci_fi=row[11],
#                 mystery=row[12],
#                 horror=row[13],
#                 documentary=row[14],
#                 biography=row[15],
#                 history=row[16],
#                 music=row[17],
#                 short=row[18],
#                 sport=row[19],
#                 war=row[20],
#                 musical=row[21],
#                 reality_tv=row[22],
#                 western=row[23],
#                 game_show=row[24],
#                 talk_show=row[25],
#                 img_link=row[26]
#             )
#     return HttpResponse('csv변환 완료')


class ListContentView(ListAPIView):
    serializer=PreferOttContentGenreSerializer
    permission_classes=(AllowAny,)

    def get(self,request):
        #선호 장르들에 선호장르 정보 모두 다 가져오기
        queryset=PreferOttContentGenre.objects.all()
        list_to_set=set([])

        while len(queryset)!=40:
            i=random.randrange(0,129)
            temp=queryset[i]
            list_to_set.add(temp)
        
        final_queryset=list(list_to_set)
        
        contents_set_serializer=PreferOttContentGenreSerializer(final_queryset,many=True)
        return Response(contents_set_serializer.data,status=status.HTTP_200_OK)

class CreateUserView(CreateAPIView):
    serializer_class=CreateUserSerializer
    permission_classes=(AllowAny,)
    
    #이 함수를 ListAPIView로 만들어야 return에서 self.list가 나옴. 따로 뺴줘야겠다.
    #유효성 검사 수행.
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#이게 db에 저장하는 코드가 맞는지?
        #여기엔 이제 user와 prefer_ott_content_genre의 연결테이블에 insert하는.
        # user=User.objects.get(username=request.data['username']).first()
        # pocg=PreferOttContentGenre.objects.get(title=request.data['title']).first()
        # user.prefer_ott_content_genres(user_id=user.id,preferottcontentgenre_id=pocg.id)
        # user.save()

        status_code=status.HTTP_201_CREATED
        response={
            'success':'true',
            'error':'null',
            'message':'회원가입 성공',
            'status_code':status_code
        }
        return Response(response,status=status_code)

# class CreateContentView(CreateAPIView):
#     serializer_class=PreferOttContentGenreSerializer
#     permission_classes=(AllowAny,)

#     def post(self, request):
#         serializer=self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.user_id=request.user.id
#         serializer.save()
#         status_code=status.HTTP_201_CREATED
#         response={
#             'success':'true',
#             'error':'null',
#             'message':'회원가입 선호장르 입력 성공',
#             'status_code':status_code
#         }
#         return Response(response,status=status_code)

class LoginUserView(GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes=(AllowAny,)

    def post(self,request):
        #deserialize.
        username=request.data.get('username')
        password=request.data.get('password')

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response={
            'success':'true',
            'error':'null',
            'status_code':status.HTTP_200_OK,
            'message':'유저 로그인 및 jwt 토큰 발급 완료!',
            'token':serializer.data['token'],
            'data':serializer.errors
        }
        status_code=status.HTTP_200_OK
        return Response(response,status=status_code)
