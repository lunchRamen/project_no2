from django.urls import path

from .views import CreateUserView,LoginUserView

app_name='apps.user'

urlpatterns=[
    path('register',CreateUserView.as_view()),
    #path('register-contents/',CreateContentView.as_view())
    path('login',LoginUserView.as_view())
]


