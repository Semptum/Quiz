from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html', {})

def available(request):
    return render(request, 'quiz/dashboard.html', {})

def dashboard(request):
    return render(request, 'quiz/dashboard.html', {})

def settings(request):
    return render(request, 'quiz/dashboard.html', {})

def login(request.POST):
    return render(request, 'quiz/dashboard.html', {})
