"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from rest_framework.Permissions import AllowAny
from rest_framework import routers,permissions


# 2. URL 매핑 : url.py 추가
# django에서 url.py는 URL 과 view 를 매핑하는 역할을 수행합니다. 프로젝트/앱은 각각의 url.py를 가질 수 있습니다.
# 프로젝트 내 url.py에 모든 URL 매핑을 수행하는 것 보다, 프로젝트는 앱들의 url을 포함하고 각각의 앱에서 디테일한 URL 매핑이 이뤄질 수 있도록 구현하는 것이 더 편리합니다.
# django 에서는 url 매핑을 path()함수를 사용하는 데, path( 'route' , 'view' ) 형식으로 사용됩니다. (django 2.0 이후)
# 첫번째 파라미터인 'route'에는 URL route에서 사용된 경로를 지정하고, 두번째 파라미터인 'view' 는 해당 URL에 매핑되는 View를 지정합니다.

schema_view = get_schema_view(
    openapi.Info(
        title="project A title", # 타이틀
        default_version='v1', # 버전
        description="설명 어쩌구저쩌구", # 설명
        terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="이메일"),
        # license=openapi.License(name=""),
    ),
    # validators=['flex'],
    public=True,
    permission_classes=(AllowAny,)
)


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    path('admin/', admin.site.urls), 
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    # django 앱 
    path('scooter', include('scooter.urls')),
    path('bus', include('bus.urls'))
]