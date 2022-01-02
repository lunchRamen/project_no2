# 여긴 user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # (경로, View 함수)
    # # 첫번째 파라미터인 'route'에는 URL route에서 사용된 경로를 지정하고, 두번째 파라미터인 'view' 는 해당 URL에 매핑되는 View를 지정합니다.
]