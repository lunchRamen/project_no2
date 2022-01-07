from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
#from .models import User,Prefer_ott_content_genre
import csv # csv 읽기 
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import ReviewScore
from apps.user.models import User
from rest_framework.permissions import IsAuthenticated
#from .serializer import CreateUserSerializer, UserSerializer, LoginUserSerializer
"""
class IndexView(APIView):
    def get(self,request):
        return JsonResponse('return success',status=200)
"""
# # 쿼리파람이 필요 없는 경우, 갖고있는 데이터로 하기
# class FirstAnalysisView(APIView):
#     def get(self,request):
#         # jwt인증 먼저 받기 거기 있는 username와 password로
# current_user = User.objects.get(username=seoyoon)
# # birthday로 age 도출하는 logic 1 필요
# # average_10s

# 1번

# 2번
"""
# 3,5,6,7번 csv DB에 넣기
def csvToModel(request):
    with open('apps/user/ott_contents.csv','r') as f:
        # rows = csv.reader(f, delimiter = ',')
        data=f.readline()
        rows=csv.reader(f,delimiter = ',')
        for row in rows:
            ReviewScore.objects.create(
                review_genre = row['genre'], 
                average_male = row['average_male'], 
                average_female = row['average_female'], 
                average_10s = row['average_10s'], 
                average_20s = row['average_20s'], 
                average_30s = row['average_30s'], 
                average_40s = row['average_40s'], 
                average_50_up = row['average_50_up']
            )
"""
"""
# 5번
class FifthAnalysisView(APIView):
    permission_classes=(IsAuthenticated, )
    def get(self,request):
        current_user=request.get['username']
        user=User.objects.get(username=current_user)
"""


