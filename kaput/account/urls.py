from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup_page, name="signup_page"),
    path('signup/', views.create_user, name="create_user"),
    path('login', views.login_user, name="login_user"),
    path('login/', views.confirm_user_login, name="confirm_user_login"),
]