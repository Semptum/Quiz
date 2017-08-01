from django.shortcuts import render, redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from quiz.models import *
from django import forms
import datetime
from .Technique import *


def prof_settings(request):
    msg = ""
    if request.POST != {}:
        nom = request.POST['nom']
        effectif = request.POST['effectif']
        id = Profs.objects.get(username = request.session['username'])
        C = Classes(effectif = effectif, idProf = id, nom = nom)
        C.save()
        msg = "Classe ajoutée."
    return render(request, 'quiz/settings.html', {"loginned" : True, "prof": True, "msg":msg})

def prof_quizzes(request):
    """
    Doit afficher la liste des quizzs de ce prof ainsi que la possibilité de créer des quizzs.
    :param request:
    :return:
    """
    prof = Profs.objects.get(username=request.session['username'])
    QuizzsExistants = Quizz.objects.filter(idProf=prof)
    L = []
    for q in QuizzsExistants:
        classe = q.idClasse.nom
        date = q.date
        url = "#"
        corr = q.correction.url
        L += [(classe,date,url)]
    if request.POST == {}:
        form = UploadFileForm()
        return render(request, 'quiz/quizzes.html', {'quizzes': L, 'form': form, 'creer': True,"loginned":True,"location":"Available"})
    else:
        televerser_quizz(request)
        return msg(request, "Quizz rajouté",{"loginned": True,"location":"Available"})

def prof_dashboard(request):
    """
    Affichage du dashboard pour les profs
    :param request:
    :return:
    """
    prof=Profs.objects.get(username=request.session['username'])
    classes=Classes.objects.filter(idProf=prof)
    ResultatsDesEleves={}
    for c in classes:
        eleves=Eleves.objects.filter(idClasse=c)
        Moyennes=[]
        for e in eleves:
            R=Resultats.objects.filter(idEleve=e)
            M=0
            n=0
            for r in R:
                n+=1
                M+=note(r)
            M/=n
            Moyennes+=[M]
        ResultatsDesEleves[c.nom] = Moyennes
    return msg(request,"Hello",{"loginned":True,"location":"Dashboard"})
