"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

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
    path("admin/", admin.site.urls),
    path("api/token/", obtain_jwt_token),
    path("api/token/verify/", verify_jwt_token),
    path("api/token/refresh/", refresh_jwt_token),
    path("api/user/", include("apps.user.urls")),
    path("api/small-theater", include("apps.small_theater.urls")),
    path("api/contents-analysis/", include("apps.contents_analysis.urls")),
    path(
        r"swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        r"swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        r"redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc-v1"
    ),
]
