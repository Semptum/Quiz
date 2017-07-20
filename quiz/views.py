from django.shortcuts import render
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from quiz.models import *

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html', {})

def available(request):
    return render(request, 'quiz/available.html', {})

def dashboard(request):
    return render(request, 'quiz/dashboard.html', {})

def settings(request):
    return render(request, 'quiz/settings.html', {})

def login(request):
    if request.POST=={}:
        return render(request, 'quiz/login.html', {})
    print(request.POST)
    user=request.POST['username']
    pswd=request.POST['password']
    hashed=pbkdf2_sha256.encrypt(pswd, rounds=200000, salt_size=16)
    classe=Classes(effectif=42,nom="MP")
    classe.save()
    eleve=Eleves(idClasse=classe,password=hashed,username=user,nom="NoName",prenom="HeyHo")
    eleve.save()
    return HttpResponse("Thanks for signing in")