from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from .serializer import CreateUserSerializer, UserSerializer, LoginUserSerializer
# 우리 view의 계층 : APIView -> GenericView -> Concrete View classes -> Viewsets

class IndexView(APIView):
    def get(self,request):
        return JsonResponse('return success',status=200)

class CreateUserView(CreateAPIView):
    serializer_class=CreateUserSerializer
    permission_classes=(AllowAny,)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code=status.HTTP_201_CREATED
        response={
            'success':'true',
            'status_code':status_code,
            'message':'유저 생성 완료'
        }
        return Response(response,status=status_code)

