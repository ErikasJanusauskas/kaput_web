from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse # удалить после темплейтов

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
    user = request.user
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
