from django.shortcuts import render
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from quiz.models import *

# Create your views here.
def index(request):
    if request.session.has_key('username'):
        return dashboard(request)
    return render(request, 'quiz/index.html', {})

def available(request):
    if request.session.has_key('username'):
        return render(request, 'quiz/available.html', {})
    return render(request, 'quiz/index.html', {})

def dashboard(request):
    if request.session.has_key('username'):
        return render(request, 'quiz/dashboard.html', {})
    return render(request, 'quiz/index.html', {})

def settings(request):
    if request.session.has_key('username'):
        return render(request, 'quiz/settings.html', {})
    return index(request)

def login(request):
    if request.session.has_key('username'):
        return dashboard(request)
    if request.POST=={}:
        return render(request, 'quiz/login.html',{})
    user=request.POST['username']
    pswd=request.POST['password']
    eleve=Eleves.objects.filter(username=user)
    if len(eleve)==0:
        return HttpResponse("Compte inexistant")
    hashed=eleve[0].password
    correct=pbkdf2_sha256.verify(pswd,hashed)
    if correct:
        request.session['username']=user
        return HttpResponse("Logged in")
    return HttpResponse("Mauvais mot de passe")

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponse("You've been logged out")

def signup(request):
    if request.POST=={}:
        L = Classes.objects.raw("SELECT id,Nom FROM quiz_classes")
        Noms = [i.Nom for i in L]
        return render(request, 'quiz/signup.html', {"noms":Noms})
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