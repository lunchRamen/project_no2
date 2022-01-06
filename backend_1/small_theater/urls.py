from django.conf.urls import url, include
from django.urls import path
from . import views #small_theater/views.py 

from django.conf import settings
from django.conf.urls.static import static

app_name = 'small_theater'

urlpatterns =[
    path('', views.SmallTheaterList.as_view()),
    path('/<int:id>',views.SmallTheaterDetail.as_view()) # http://127.0.0.1:8000/small-theater/4 앞에 슬래시 없애면 small-theater4로 들어감
]
