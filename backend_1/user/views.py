from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view #api
from rest_framework.response import Response #api
# 장고는 return HttpResponse 등의 표현을 쉽게 쓸 수 있도록 render 함수를 제공하는데요.
# 일일히 HttpResponse 를 정의하지 않고도 쉽게 HttpResponse 에 응답할 수 있습니다.

# 0. MVT 패턴. Model은 데이터 모델을 의미하며, migrate를 수행하면 DB에 바로 수정반영됩니다. (추후 포스팅 예정) View는 Controller역할을 수행하며, 모델의 데이터를 받아 template에 뿌리기전 연산을 수행합니다. Template은 바로 사용자에게 보여주는 뷰(view)에 해당하며 html 등을 의미합니다.

# 2. 장고의 뷰(View)는 웹애플리케이션의 "로직" 부분을 담당하여 동작합니다.
# 즉, 내 애플리케이션을 동작하게 하기 위해 CRUD(Create/Read/Update/Delete) 등 함수를 구현하는 곳입니다!
# 또한, django 는 MVT(Model-View-Template) 패턴에 기반하여 동작하는데요.
# View는 유명한 패턴 중의 하나인 MVC 패턴의 Controller 역할을 수행한다고 보시면 됩니다 :)

# 3. FBV(Function Based View) 이기 때문에, API 데코레이터인 @api_view(['GET'])으로 선언해 주어야 swagger에서 인식합니다.  저와 같은 FBV 기반 프로젝트는 @api_view 데코레이터를 사용하여 API 뷰를 짜야 하며, CBV 기반 프로젝트는 APIView 클래스를 사용하여  API 뷰를 짜야 합니다 :D 

# Create your views here.

# Response : JsonResponse, HttpResponse 객체가 모두 Response로 대체되었고, 각 Response 객체에 넘기는 status 인자에 단순 숫자 상태 코드가 아닌 status 객체의 식별자로 대체된 것이다.
def index(request):
    return HttpResponse("Hi This is Seoyoon's User page")

@api_view(['GET'])
def get(request):
    return Response(request.data)

@api_view(['POST'])
def post(request):
    return Response(request.data)
