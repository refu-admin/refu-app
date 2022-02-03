import django
import django.contrib.auth.views
from django.urls import path,include
from . import views

app_name='refuapp'

urlpatterns=[
    path('top/',views.top_page, name="top"),
    # path('index/', views.index, name='index'),# リダイレクト
    path('login/', # ログイン
     django.contrib.auth.views.LoginView.as_view(template_name = 'user_auth/login.html'),
     name='login'),
    path('logout/', # ログアウト
     django.contrib.auth.views.LogoutView.as_view(template_name = 'user_auth/login.html'),
     name='logout'),
]