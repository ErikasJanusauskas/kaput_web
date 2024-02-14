from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Quizzes, Questions
from account.models import Profile

# Create your views here.
def index(request):
    return render(request, 'quiz.html')

def quest(request, quizID, questID):
    user=request.user
    if user.is_authenticated:
        if request.method == "POST":
            print("POST")
            user_answer = request.POST.get("answer")
            print(user_answer)
            if user_answer != None:
                question = Questions.objects.get(id=(questID-1))
                Profile.objects.create(user=user, question=question, answer=user_answer)
            else:
                return redirect("quest", quizID=quizID,  questID=questID-1)
        try:
            quiz  = Quizzes.objects.get(id=quizID)
            quest = Questions.objects.get(id=questID)
            context = {
            "quiz": quiz,
            "quest":quest,
            "previous":quest.id-1,
            "next":quest.id+1
        }
        except:
            return redirect("profile")
    else:
        return redirect("login_user")
    return render(request, 'question.html', context)