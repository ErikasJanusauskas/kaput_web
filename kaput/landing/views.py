from django.shortcuts import render, redirect
from quiz.models import *

# Create your views here.
def index(request):
    first = []
    quizzes = Quizzes.objects.all()
    for quiz in quizzes:
        fQuest = Questions.objects.filter(quiz=quiz.id)[:1]
        fQuest = fQuest[0].id
        questions = len(Questions.objects.filter(quiz=quiz.id))
        first.append(fQuest)
    
    context = {
        "looping": zip(quizzes, first),
        "total" : questions
    }

    return render(request, 'landing.html', context)