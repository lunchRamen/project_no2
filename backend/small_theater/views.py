from django.shortcuts import render
from django.views import generic
from rest_framework.decorators import api_view # @api_view

# FBV와 Generic View가 있음
# FBV는 세세하게 코딩/ Generic view는 간편 -> 섞어도 됨

# 3. FBV(Function Based View) 이기 때문에, API 데코레이터인 @api_view(['GET'])으로 선언해 주어야 swagger에서 인식합니다.  저와 같은 FBV 기반 프로젝트는 @api_view 데코레이터를 사용하여 API 뷰를 짜야 하며, CBV 기반 프로젝트는 APIView 클래스를 사용하여  API 뷰를 짜야 합니다 :D 

# 클래스형 뷰 참고사이트
# https://coshin.tistory.com/13

# Create your views here.

class Index(generic.TemplateView): #제너릭뷰 사용중
    def index(self,request,*args,**kwargs):
        result = request.data
        return render(result,'./templates/index.html')

def index(request):
    return HttpResponse("Sixmen's Small Theater page")

# def index(request):
#     return render(request,'small_theater/templates/index.html')

@api_view(['GET'])
def get(request):
    return Response(request.data)

@api_view(['POST'])
def post(request):
    return Response(request.data)