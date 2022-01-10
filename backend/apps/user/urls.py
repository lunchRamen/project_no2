from django.urls import path

from .views import CreateUserView, ListContentView, LoginUserView  # csv다운 시 주석하기

app_name = "apps.user"

urlpatterns = [
    path("register", CreateUserView.as_view()),  # csv주석
    path("login", LoginUserView.as_view()),  # csv 주석
    path("contents-list", ListContentView.as_view()),  # csv 주석
]
