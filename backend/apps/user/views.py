import csv
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView, View

# Create your views here.
from .models import PreferOttContentGenre, User
from .serializer import (
    CreateUserSerializer,
    LoginUserSerializer,
    PreferOttContentGenreSerializer,
)

"""
View에도 Model처럼 4계층으로 상속이 진행됨.
APIView -> GenericView -> Concrete View classes -> Viewsets
"""


class ListContentView(ListAPIView):
    serializer_class = PreferOttContentGenreSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        # 선호 장르들에 선호장르 정보 모두 다 가져오기
        queryset = PreferOttContentGenre.objects.all()
        list_to_set = set([])

        while len(list_to_set) != 40:
            i = random.randrange(0, 129)
            temp = queryset[i]
            list_to_set.add(temp)

        return list_to_set


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)


class LoginUserView(APIView):
    """
    로그인

    아이디, 비밀번호를 입력받아 로그인 합니다.
    """

    serializer_class = LoginUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        # deserialize.

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            "success": "true",
            "error": "null",
            "status_code": status.HTTP_200_OK,
            "message": "유저 로그인 및 jwt 토큰 발급 완료!",
            "token": serializer.data["token"],
            "data": serializer.errors,
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
