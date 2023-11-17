from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
from django.views.generic import DetailView
from django.db import models
from django.contrib.auth.models import User


class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'index.html'
    context_object_name = 'question'

# Create your views here.


def homepage(request):
    questions = Questions.objects.all()
    return render(request, 'index.html', {'questions':questions})

def dbtest(request):
    questionsList = Questions.objects.all()
    qTitle = questionsList[0].title
    return render(request, 'dboutouttest.html', {'qTitle':qTitle})

def authtest(request):
    return render(request, 'authtest.html')

def getform(request):
    if request.method == "POST":
        firstName = request.POST.get("fistName")
        secondName = request.POST.get("lasName")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        email = request.POST.get("email")
        print(firstName)
        userData = [firstName, secondName, password, password_confirm, email]
        user = User.objects.create_user(firstName, email, password)
    return render(request, 'index.html', {'userData':userData}) 