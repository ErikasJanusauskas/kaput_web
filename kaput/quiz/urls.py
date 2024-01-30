from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:quizID>/<int:questID>', views.quest, name='quest')
]