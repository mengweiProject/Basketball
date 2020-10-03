"""Basketball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('second/', views.second),
    path('manage/', views.manage),
    path('words/', views.words),
    path('index/', views.index),
    path('register/', views.register),
    path('publisher/', views.publisher),
    path('add/', views.add),
    path('img/', views.show_one_img),
    path('player_info/', views.player_info),
    path('del_player/', views.del_player),
    path('add_player/', views.add_player),
    path('modify_player/', views.modify_player),
    path('page1/', views.page1),
    path('team_list/', views.team_list),
    path('team_info/', views.team_info),
]

