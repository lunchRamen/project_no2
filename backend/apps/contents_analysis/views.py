from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
#from .models import User,Prefer_ott_content_genre
import csv # csv 읽기 
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import ReviewScore, ReviewScoreT
from apps.user.models import User
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny #로그인했는지 확인 
from .serializer import ThirdReviewScoreSerializer ,FifthReviewScoreSerializer

# # 3,5,6,7번 csv DB에 넣기
# 삭제하지 마세용!! 최초 1회 실행하기
# def csvToModel(request):
#     with open('apps/contents_analysis/Ver3_naver_review_analysis_altimate.csv','r') as f:
#         # rows = csv.reader(f, delimiter = ',')
#         data=f.readline()
#         rows=csv.reader(f,delimiter = ',')
#         for row in rows:
#             ReviewScoreT.objects.create(
#                 review_genre = row[0], 
#                 average_male = row[1], 
#                 average_female = row[2], 
#                 average_10s = row[3], 
#                 average_20s = row[4], 
#                 average_30s = row[5], 
#                 average_40s = row[6], 
#                 average_50_up = row[7]
#                 )
#     return HttpResponse('csv 다운받기 성공')

# 삭제하지 마세용!! 최초 1회 실행하기
# def csvToModel(request):
#     with open('apps/contents_analysis/T_Ver3_naver_review_analysis_altimate.csv','r') as f:
#         # rows = csv.reader(f, delimiter = ',')
#         data=f.readline()
#         rows=csv.reader(f,delimiter = ',')
#         for row in rows:
#             ReviewScoreT.objects.create(
#                 people= row[0],
#                 drama= row[1],
#                 comedy= row[2],
#                 action= row[3],
#                 thriller= row[4],
#                 romance= row[5],
#                 crime= row[6],
#                 adventure= row[7],
#                 animation= row[8],
#                 fantasy= row[9],
#                 family= row[10],
#                 sci_fi= row[11],
#                 mystery= row[12],
#                 horror= row[13],
#                 documentary= row[14],
#                 biography= row[15],
#                 history= row[16],
#                 music= row[17],
#                 short= row[18],
#                 sport= row[19],
#                 war= row[20],
#                 musical= row[21],
#                 western= row[22]
#                 )
#     return HttpResponse('csv 다운받기 성공')

# 1번 -> 프론트분이 png 띄울 것 로그인된 유저가 맞는지만 확인해줬다.
# class FirstAnalysisView(APIView):
#     permission_classes=(AllowAny,)
#     # permission_classes=(IsAuthenticated, )
#     def get(self,request):
#         current_user=request.get['username']  # 현재토큰있는애
#         user=User.objects.get(username=current_user) # 등록된애
#         # return JsonResponse('return success 1st analysis',status=200)

#         target_analysis_serializer = ReviewScoreSerializer(final_queryset, many=True)
#         return Response(target_analysis_serializer.data, status=status.HTTP_200_OK)
# # 2번 -> 프론트분이 png 띄울 것 로그인된 유저가 맞는지만 확인해줬다.
# class SecondAnalysisView(APIView):
#     permission_classes=(AllowAny,)
#     # permission_classes=(IsAuthenticated, )
#     def get(self,request):
#         # current_user=request.get['username']  # 현재토큰있는애 - 현재 로그인 된 유저는 current_user다. 변수도 같은 변수 상속?받아서 쓸 수 있기 떄문
#         # user=User.objects.get(username=current_user) # 등록된애 - 지금 로그인 된 유저1의 객체를 가져와라~
#         return JsonResponse('return success 2nd analysis',status=200)

# 3번 ReviewScoreT
class ThirdAnalysisView(APIView): # http://127.0.0.1:8000/api/contents-analysis/third-analysis?search-gender=average_male&search-age=average_20s
    permission_classes=(AllowAny,)
    # permission_classes=(IsAuthenticated, )
    def get(self,request):
        # current_user=request.GET.get('username')  # 현재토큰있는애
        # user=User.objects.get(username=current_user) # 등록된애
        search_gender = request.GET.get('search-gender')
        search_age = request.GET.get('search-age')
        if (search_gender==None) & (search_age==None):
            queryset = ReviewScoreT.objects.all()
        else:
            queryset = ReviewScoreT.objects.filter(Q(people=search_gender)|Q(people=search_age))
        target_analysis_serializer = ThirdReviewScoreSerializer(queryset, many=True)
        return Response(target_analysis_serializer.data, status=status.HTTP_200_OK)

# # 4번 -> 프론트분이 png 띄울 것 로그인된 유저가 맞는지만 확인해줬다.
# class FourthAnalysisView(APIView):
#     permission_classes=(AllowAny,)
#     # permission_classes=(IsAuthenticated, )
#     def get(self,request):
#         # current_user=request.get['username']  # 주석해제 - 현재 로그인 된 유저는 current_user다. 변수도 같은 변수 상속?받아서 쓸 수 있기 떄문
#         # user=User.objects.get(username=current_user) # 주석해제 - 지금 로그인 된 유저1의 객체를 가져와라~
#         return JsonResponse('return success 4th analysis',status=200)


# 5번 ReviewScore
class FifthAnalysisView(APIView):
    permission_classes=(AllowAny,)
    # permission_classes=(IsAuthenticated, ) #로그인 한 사람만 하게끔(small-theater는 AlloAny였다.)
    def get(self,request):
        # current_user=request.get['username']  # 현재토큰있는애
        # user=User.objects.get(username=current_user) # 등록된애
        # return JsonResponse('return success 5th analysis',status=200)
        queryset = ReviewScore.objects.filter()
        target_analysis_serializer = FifthReviewScoreSerializer(queryset, many=True)
        return Response(target_analysis_serializer.data, status=status.HTTP_200_OK)



# 6번 ReviewScore


# 7번 ReviewScore


