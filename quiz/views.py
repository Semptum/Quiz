from django.shortcuts import render, redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from quiz.models import *
from django import forms
import datetime

from .Technique import *
from .Eleves import *
from .Profs import *


# Create your views here.
def index(request):
    if request.session.has_key('username'):
        return dashboard(request)
    return render(request, 'quiz/index.html', {"loginned": False})


def available(request):
    return profeleve(request,eleve_quizzes,prof_quizzes)

def dashboard(request):
    return profeleve(request,eleve_dashboard,prof_dashboard)

def settings(request):
    if not request.session.has_key('username'):
        return index(request)
    return profeleve(request, eleve_settings, prof_settings)

def login(request):
    if request.session.has_key('username'):
        return dashboard(request)
    if request.POST=={}:
        return render(request, 'quiz/login.html',{"loginned":False})
    user=request.POST['username']
    pswd=request.POST['password']
    eleves=list(Eleves.objects.filter(username=user))
    profs=list(Profs.objects.filter(username=user))
    if len(eleves)!=0 and len(profs)==0:
        u=eleves[0]
        status="eleve"
    elif len(eleves)==0 and len(profs)!=0:
        u=profs[0]
        status="prof"
    else:
        return msg(request,"Compte inexistant",{"loginned":False})
    hashed=u.password
    correct=pbkdf2_sha256.verify(pswd,hashed)
    if correct:
        request.session['username']=user
        request.session['status']=status
        return redirect(dashboard)
    return msg(request,"Mauvais mot de passe",{"loginned":False})

def logout(request):
    try:
        del request.session['username']
        del request.session['status']
    except:
        pass
    return msg(request,"Vous avez été logouté",{"loginned":False})

def signup(request):
    if request.POST=={}:
        L = Classes.objects.raw("SELECT id,Nom FROM quiz_classes")
        Noms = [i.Nom for i in L]
        return render(request, 'quiz/signup.html', {"noms":Noms,"loginned":False})
    user=request.POST['username']
    pswd=request.POST['password']
    nom = request.POST['last name']
    prenom =request.POST['first name']
    statut = str(request.POST['statut'])
    if statut=="Eleve":
        classe = request.POST['classe']
    deja=list(Profs.objects.filter(username=user))+list(Eleves.objects.filter(username=user))

    if deja!=[]:
        return render(request,'quiz/erreur.html',{'error':"Utilisateur deja existant","loginned":False})
    hashed=pbkdf2_sha256.encrypt(pswd, rounds=200000, salt_size=16)
    if statut == "Eleve":
        t = Classes.objects.get(nom = classe)
        eleve = Eleves(nom = nom, prenom = prenom, password = hashed, username = user, idClasse = t )
        eleve.save()
    else :
        prof = Profs(nom = nom, prenom = prenom, password = hashed, username = user)
        prof.save()
    text = "Merci de votre inscription. Vous allez recevoir un email de confirmation vous permettant d'activer votre compte."
    return msg(request,text,{"loginned": False})

