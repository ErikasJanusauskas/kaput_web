from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from . models import *
from quiz.models import Questions

def signup_page(request):
    error = None
    user = request.user
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwordConf = request.POST.get("passwordConf")
        if password == passwordConf:
            try:
                User.objects.create_user(username, None, password)
                return redirect("login_user")
            except:
                error = f"Username {username} is already taken."
        else:
            error = "Your password didn't match confirming password."
        pass
    else:
        if user.is_authenticated:
            logout(request)
    context = {
                    "error":error
                }
    return render(request, "signup.html", context)

def login_user(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect("index")
        else:
            error = "Something went wrong. Please try again."
    context = {
        "error":error
    }
    return render(request, "login.html", context)


def profile(request):
    ## FOR ERIKAS:
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.filter(user=user.id)
        context = {"profile":profile}
        return render(request, "profile.html", context)
    else:
        return redirect("login_user")

def answer(request, userID, profileID):
    ## FOR ERIKAS 2
    user = request.user
    if user.is_authenticated:
        questions = Profile.objects.get(id=profileID)
        quizQuestion = Questions.objects.get(id=questions.question.id)
        if questions.answer == 1:
            questions.answer = quizQuestion.answer_1
        if questions.answer == 2:
            questions.answer = quizQuestion.answer_2
        if questions.answer == 3:
            questions.answer = quizQuestion.answer_3
        if questions.answer == 4:
            questions.answer = quizQuestion.answer_4

        if quizQuestion.answer_r == 1:
            quizQuestion.answer_r = quizQuestion.answer_1
        if quizQuestion.answer_r == 2:
            quizQuestion.answer_r = quizQuestion.answer_2
        if quizQuestion.answer_r == 3:
            quizQuestion.answer_r = quizQuestion.answer_3
        if quizQuestion.answer_r == 4:
            quizQuestion.answer_r = quizQuestion.answer_4
        context = {"question":questions, "quizQuestion":quizQuestion}
        return render(request, "answers.html", context)
    else:
        return redirect("login_user")
    