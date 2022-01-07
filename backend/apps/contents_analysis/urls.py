from django.urls import path

from .views import FifthAnalysisView, IndexView

#app_name='user'

urlpatterns=[
    path('index',IndexView.as_view()),
    path('/fifth-analysis',FifthAnalysisView.as_view()),
]