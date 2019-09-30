from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice

def index(request):
    all_questions = Question.objects.all()
    return render(request, 'index.html', {'questions': all_questions})

def register(request):
    return render(request, 'register.html')

def layout(request):
    return render(request, 'layout.html')

def about(request):
    return render(request, 'about.html')


def question(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'question.html', {"question": question})