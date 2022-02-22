import django
import django.contrib.auth.views
from django.urls import path,include
from . import views

app_name='user_auth'

urlpatterns=[
     path('',views.index, name = "default"),
     # path('', views.top, name='index'),
     path('top/',views.Command.handle, name="top"), # リダイレクト
     # path('login/', # ログイン
     # django.contrib.auth.views.LoginView.as_view(template_name = 'user_auth/login.html'),
     # name='login'),
     # path('logout/', # ログアウト
     # django.contrib.auth.views.LogoutView.as_view(template_name = 'user_auth/logout.html'),
     # name='logout'),
     path('tweet/',views.tweet, name = 'tweet'),
     # path('login/',views.signin, name = 'signin'),
     # # path('app/',views.app, name = 'app'),
     # path('callback/',views.callback, name = 'callback'),
]