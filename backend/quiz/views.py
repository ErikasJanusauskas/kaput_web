from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
from django.views.generic import DetailView


class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'index.html'
    context_object_name = 'question'

# Create your views here.


def homepage(request):
    questions = Questions.objects.all()
    return render(request, 'index.html', {'questions':questions})