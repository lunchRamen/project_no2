from django.conf.urls import url, include
from django.urls import path
from . import views #small_theater/views.py 

from django.conf import settings
from django.conf.urls.static import static

app_name = 'small_theater'

urlpatterns =[
    # url(r'^$', views.Index.as_view(), name='Index'),
    path('/', views.SmallTheaterList.as_view())
]
