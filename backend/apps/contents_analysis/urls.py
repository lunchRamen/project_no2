from django.urls import path

from .views import IndexView

#app_name='user'

urlpatterns=[
    path('index/',IndexView.as_view()),
]