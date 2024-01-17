from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Quizzes, Questions

# Create your views here.
def index(request):
    return render(request, 'quiz.html')

def quizGeneral(request, quizID):
    quiz = Quizzes.objects.get(id=quizID)
    context = {
        'quizName':quiz.name
    }
    return render(request, 'quiz.html', context)

def quest(request, quizID, questID):
    quiz  = Quizzes.objects.get(id=quizID)
    quest = Questions.objects.get(id=questID)
    context = {
        'quizName': quiz.name,
        'quest':quest.name,
        'answer_1':quest.answer_1,
        'answer_2':quest.answer_2,
        'answer_3':quest.answer_3,
        'answer_4':quest.answer_4,
    }