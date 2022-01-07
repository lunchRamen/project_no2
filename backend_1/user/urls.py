# 여긴 user/urls.py
from django.urls import path
from . import views
# FBV로 만들면 @api_view로 GET인지 POST인지 선언해줘야 swagger에서 인식한다.
app_name = 'user'
urlpatterns = [
    path('/', views.index, name='index'),# path(경로, View 함수)
    path('/get_url', views.get, name='get'), 
    # # 첫번째 파라미터인 'route'에는 URL route에서 사용된 경로를 지정하고, 두번째 파라미터인 'view' 는 해당 URL에 매핑되는 View를 지정합니다.
    path('/post_url',views.post, name='post'),
]
