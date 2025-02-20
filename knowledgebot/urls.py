from django.contrib import admin
from django.urls import path, include
from .views import knowledgebot_home, register, login_view, logout_view

urlpatterns = [
    path("", knowledgebot_home, name="knowledgebot_home"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]