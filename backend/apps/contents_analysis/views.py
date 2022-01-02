from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
#from .models import User,Prefer_ott_content_genre

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
#from .serializer import CreateUserSerializer, UserSerializer, LoginUserSerializer

class IndexView(APIView):
    def get(self,request):
        return JsonResponse('return success',status=200)