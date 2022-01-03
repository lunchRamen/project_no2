from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'small_theater'

urlpatterns =[
    url(r'^$', views.Index.as_view(), name='Index'),
]
