from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup_page, name="signup_page"),
    path('login', views.login_user, name="login_user"),
    path('profile', views.profile, name="profile"),
    path('<userID>/<questionID>', views.answer, name="answer")
]