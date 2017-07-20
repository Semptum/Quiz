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
        L = Classes.objects.raw("SELECT id,Nom FROM quiz_classes")
        Noms = [i.Nom for i in L]
        return render(request, 'quiz/login.html', {"noms":Noms})
    user=request.POST['username']
    pswd=request.POST['password']
    nom = request.POST['last name']
    prenom =request.POST['first name']
    classe = request.POST['classe']
    hashed=pbkdf2_sha256.encrypt(pswd, rounds=200000, salt_size=16)
    t = Classes.objects.filter(nom = classe)
    eleve = Eleves(nom = nom, prenom = prenom, password = hashed, username = user, idClasse = t[0] )
    eleve.save()
    return HttpResponse("Merci de votre inscription")