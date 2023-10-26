from django.shortcuts import render
from django.http import HttpResponse
# from . import models

# Create your views here.


def homepage(request):
    # questions = Questions.objects.all()
    # testtext = questions[0].title
    return render(request, 'index.html')