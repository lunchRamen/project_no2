from django.urls import path

from .views import CreateUserView,CreateContentView

app_name='apps.user'

urlpatterns=[
    path('register/',CreateUserView.as_view()),
    path('register-contents/',CreateContentView.as_view())
]

