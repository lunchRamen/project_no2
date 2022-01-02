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
from django.urls import path,include,re_path
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token,refresh_jwt_token
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view( 
    openapi.Info( 
        title="Sixmen API 문서화", 
        default_version="1.0.0", 
        description="Sixmen에서 FE와 BE의 데이터 호출 응답 통일을 위한 Swagger사용.", 
        terms_of_service="https://www.google.com/policies/terms/", 
#        contact=openapi.Contact(name="test", email="test@test.com"), 
#        license=openapi.License(name="Test License"), 
    ), 
    public=True, 
    permission_classes=[permissions.AllowAny], 
)

# apps_urls=[
#     path('',include('apps.user.urls')),
#     path('small_theater/',include('small_theater.urls')),
#     path('contents_analysis',include('contents_analysis.urls')),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/user/',include('apps.user.urls')),
    path('api/small_theater/',include('apps.small_theater.urls')),
    path('api/contents_analysis/',include('apps.contents_analysis.urls')),
    # path('api/',include('apps_urls')),
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'), 
]

# 이건 디버그일때만 swagger 문서가 보이도록 해주는 설정이라는 듯. urlpath도 이 안에 설정 가능해서, debug일때만 작동시킬 api도 설정할 수 있음.
# if settings.DEBUG:
#     urlpatterns += [
#         re_path(
#             r"^swagger(?P<format>\.json|\.yaml)$",
#             schema_view.without_ui(cache_timeout=0),
#             name="schema-json",
#         ),
#         re_path(
#             r"^swagger/$",
#             schema_view.with_ui("swagger", cache_timeout=0),
#             name="schema-swagger-ui",
#         ),
#         re_path(
#             r"^redoc/$",
#             schema_view.with_ui("redoc", cache_timeout=0),
#             name="schema-redoc",
#         ),
#     ]
