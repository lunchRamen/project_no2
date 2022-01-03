"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import url
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework import routers,permissions


# 2. URL 매핑 : url.py 추가
# django에서 url.py는 URL 과 view 를 매핑하는 역할을 수행합니다. 프로젝트/앱은 각각의 url.py를 가질 수 있습니다.
# 프로젝트 내 url.py에 모든 URL 매핑을 수행하는 것 보다, 프로젝트는 앱들의 url을 포함하고 각각의 앱에서 디테일한 URL 매핑이 이뤄질 수 있도록 구현하는 것이 더 편리합니다.


schema_url_patterns = [ # swagger에서 API 문서로 보고싶은 URL들을 정의합니다.
    path('user/',include('user.urls')),
]

schema_view = get_schema_view(  
    openapi.Info(
        title="Sixmen API 문서", # 프로젝트 이름
        default_version='1.0.0', # 프로젝트 버전 ex) 1.1.1
        description="Sixmen프로젝트 FE-BE 간 호출 응답을 위한 Open API", # 설명
        terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="이메일"),
        # license=openapi.License(name=""),
    ),
    # validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns = schema_url_patterns, # 오류 떠서 주석처리 해놓음 
)

app_name = 'user'
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [ # swagger를 보기 위한 엔드포인트를 정의합니다. 
# include() 함수는 다른 URLconf들을 참조할 수 있도록 해주고 Django가 함수 include()를 만나게 되면 설정된 url(/apps) 뒤의 url들에 대한 처리를 위하여 app.urls.py인 URLconf로 전달하는 역할을 합니다.

# 기본적으로 URL관련한 구조를 살펴보면 localhost:8000/user의 경우
# 1. urls.py(jackerlab_django/urls.py)의 설정을 확인하고 여기의 /user 설정에 따라
# 2. user/urls.py를 바라보게되고
# 3. user/urls.py의 URL 설정에 따라 동작을 하게 됩니다.

    #django앱
    path('admin/', admin.site.urls), 
    # path('user', include('user.urls')),
    # 첫번째 파라미터인 'route'에는 URL route에서 사용된 경로를 지정하고, 두번째 파라미터인 'view' 는 해당 URL에 매핑되는 View를 지정합니다.

    #react 
    re_path('.*', TemplateView.as_view(template_name='index.html')),
    
    #swagger
    url(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]