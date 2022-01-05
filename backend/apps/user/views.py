from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .models import User,PreferOttContentGenre

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from .serializer import CreateUserSerializer, UserSerializer, LoginUserSerializer

"""
View에도 Model처럼 4계층으로 상속이 진행됨.
APIView -> GenericView -> Concrete View classes -> Viewsets
"""

class IndexView(APIView):
    def get(self,request):
        return JsonResponse('return success',status=200)

class CreateUserView(CreateAPIView):
    serializer_class=CreateUserSerializer
    permission_classes=(AllowAny,)

    #유효성 검사 수행.
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#이게 db에 저장하는 코드가 맞는지?
        status_code=status.HTTP_201_CREATED
        response={
            'success':'true',
            'error':'null',
            'message':'회원가입 성공',
            'status_code':status_code
        }
        return Response(response,status=status_code)





