from django.shortcuts import render, redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from quiz.models import *
from django import forms
import datetime
from .Technique import *

def eleve_settings(request):
    return render(request, 'quiz/settings.html', {"loginned":True,"prof":False})


def eleve_quizzes(request):
    """
    Fonction qui affiche la page des quizzs de l'eleve. Elle doit lui montrer les quizzs deja faits et
    les quizzs qu'il doit faire. Elle doit aussi bien ne montrer que la correction
    des quizzs deja faits. Elle doit donner les liens vers une page dynamique qui va afficher le quizz de facon a le passer
    :param request:
    :return:
    """
    eleve = Eleves.objects.get(username=request.session['username'])
    classe = eleve.idClasse
    QuizzsExistants = list(Quizz.objects.filter(idClasse=classe))
    L = []
    for q in QuizzsExistants:
        classe = q.idClasse.nom
        date = q.date
        url = q.quizz
        corr = q.correction
        L += ["Quizz posé le " + str(date) + " a la classe " + classe + ": " + url + " . Correction: " + corr]
    return render(request, 'quiz/available.html', {'quizzes': L,"loginned":True,"location":"Available"})


def eleve_dashboard(request):
    """
    Fonction qui affiche le dashboard des eleves. A completer
    :param request:
    :return:
    """
    eleve=Eleves.objects.get(username=request.session['username'])
    resultats=Resultats.objects.filter(idEleve=eleve)
    Notes=[note(r) for r in resultats]
    return render(request,'quiz/dashboard.html',{'est_eleve':True,'notes':Notes,"loginned":True,"location":"Dashboard"})

