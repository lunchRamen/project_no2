from urllib import parse

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SmallTheater
from .serializer import SmallTheaterSerializer

# Create your views here.


class SmallTheaterList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, **kwargs):
        search_keyword = request.GET.get("search-keyword")
        for key in request.GET.keys():
            if request.GET.get(key) is not None:
                parse.unquote(request.GET.get(key))

        # 1. genre1,genre2,title 셋 다 None인 경우
        if search_keyword is None:
            final_queryset = SmallTheater.objects.all().order_by(
                "-published_date"
            )  # /small-theater

        # 2. title이 있는 경우(__contains오류 떄문에 얘만 따로)
        elif search_keyword:
            queryset = SmallTheater.objects.filter(
                Q(theater_genre1=search_keyword)  # noqa
                | Q(theater_genre2=search_keyword)  # noqa
                | Q(title__contains=search_keyword)  # noqa
            )  # 단어포함 title__contains = 어쩌구
            final_queryset = queryset.order_by(
                "-published_date"
            )  # published_date하면 오름차순

        target_theater_serializer = SmallTheaterSerializer(final_queryset, many=True)
        return Response(target_theater_serializer.data, status=status.HTTP_200_OK)


class SmallTheaterDetail(APIView):  # 소극장 상세보기
    # http://127.0.0.1:8000/small-theater/3
    permission_classes = (AllowAny,)

    def get(
        self, request, **kwargs
    ):  # http://localhost:8000/small-theater/{small_theater.id}
        target_theater_id = kwargs.get("id")  # 4 (int)
        queryset = SmallTheater.objects.filter(
            id=target_theater_id
        )  # get은 하나만 가져옴 not iterable이슈 있음
        target_theater_serializer = SmallTheaterSerializer(queryset, many=True)
        return Response(target_theater_serializer.data, status=status.HTTP_200_OK)
