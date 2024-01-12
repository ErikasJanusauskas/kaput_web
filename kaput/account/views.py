from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse # удалить после темплейтов

def signup_page(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
    return HttpResponse('sign up page')
        
def  create_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('signup_page')
    if request.method == "POST":
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm:
            username = request.POST.get('username')
        try:
            new_user = User.objects.create_user(username, None, password)
        except:
            return HttpResponse(f'ERROR INFO: cannot create user: \nUsername:{username}\nPassword:{password}\nEmail:{None}')
    else:
        return HttpResponse('missmatch between password and password confirm fields')
    return HttpResponse('user created')

def login_user(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse('log in page')
    else:
        return HttpResponse('redirect to user profile')

def confirm_user_login(request):
    user = request.user
    if not user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_auth = authenticate(request, username=username, password=password)
            if user_auth is not None:
                login(request, user)
                return HttpResponse(f'user {username} is authenticated')
            else:
                return HttpResponse(f'ERROR INFO: cannot authenticate user:\nUsername: {username}\nPassword: {password}')
    else:
        return HttpResponse('redirect to user profile')