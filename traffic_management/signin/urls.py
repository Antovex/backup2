from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('errorpage', views.errorpage, name="errorpage"),
    path('', views.signin, name="signin"),
    path('register', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
]
