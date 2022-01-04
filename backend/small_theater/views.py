from django.http import response
from django.shortcuts import render
from django.views import generic
from rest_framework.decorators import api_view # @api_view
from rest_framework import Response
from .models import SmallTheater
# FBV와 Generic View가 있음
# FBV는 세세하게 코딩/ Generic view는 간편 -> 섞어도 됨

# 3. FBV(Function Based View) 이기 때문에, API 데코레이터인 @api_view(['GET'])으로 선언해 주어야 swagger에서 인식합니다.  저와 같은 FBV 기반 프로젝트는 @api_view 데코레이터를 사용하여 API 뷰를 짜야 하며, CBV 기반 프로젝트는 APIView 클래스를 사용하여  API 뷰를 짜야 합니다 :D 

# 클래스형 뷰 참고사이트
# https://coshin.tistory.com/13

# static, 템플릿 등 참고사이트 https://iamiet.tistory.com/10?category=928115

# Create your views here.

class SmallTheaterList(generic.View): #제너릭뷰 사용중
    def get(self,request): #클래스형은 GET,POST등 할 때 함수이름을 꼭 GET으로 해야되나봄
        result = request # WSGIRequst(클래스형get) object는 data속성이 없다
        template_name = 'small_theater/index.html'
        small_theater_list = SmallTheater.objects.all() #ORM 통해 쿼리셋 가져오기 
        contents = {
            'small_theater_list':small_theater_list,
        } #딕셔너리로 만들기
        response
        return render(result,template_name, contents)
        # render의 3번쨰 인자는 딕셔너리여야한다.

class SmallTheaterDetail(generic.DetailView):
    model = SmallTheater
    template_name = 'small_theater/detail.html'
    context_object_name = 'small_theater'

@api_view(['GET'])
def index(request):
    return HttpResponse("Sixmen's Small Theater page")

# def index(request):
#     return render(request,'small_theater/index.html')

@api_view(['GET'])
def get(request):
    return Response(request.data)

@api_view(['POST'])
def post(request):
    return Response(request.data)