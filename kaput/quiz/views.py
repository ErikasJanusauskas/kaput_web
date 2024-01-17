from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user = User.objects.get(username='alex.pm')
    user.set_password('admin.pm')  # Замените 'новый_пароль' на ваш новый пароль
    user.save()
    return render(request, 'quiz.html')