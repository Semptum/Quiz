from django.shortcuts import render, redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from quiz.models import *
from django import forms
import datetime

class UploadFileForm(forms.Form):
    file = forms.FileField()
    corr = forms.FileField()
    classe=forms.CharField(max_length=10)


def msg(request,message):
    """
    Simple fonction qui affiche le message
    :param request:
    :param message:
    :return:
    """
    return render(request,'quiz/message.html',{'msg':message})

def televerser(file):
    """
    Fonction qui doit etre complétée. Elle doit renvoyer le lien vers l'endroit ou se trouve le fichier apres televersement
    :param file:
    :return:
    """
    return "http://blaisepascal-prepa.forumactif.org/"

def profeleve(request,f_eleve,f_prof):
    """
    Fonction qui verifie si on est loginé (sinon elle nous renvoie a index. Si on l'est, elle verifie notre statut. Si on est prof elle va executer f_prof.
    Sinon, ce sera f_eleve.
    :param request:
    :param f_eleve:
    :param f_prof:
    :return:
    """
    if not request.session.has_key('username'):
        return render(request, 'quiz/index', {})
    status=request.session['status']
    if status=="prof":
        return f_prof(request)
    return f_eleve(request)

def redirection(request,normal,defaut):
    """
    Fonction un peu inutile qui redirige vers "default" si on est pas loginé, et "normal" sinon.
    :param request:
    :param normal:
    :param defaut:
    :return:
    """
    if request.session.has_key['username']:
        return normal(request)
    return defaut(request)

def note(resultat):
    """
    Fonction qui prend l'objet resultat et qui donne une note. Elle est aussi capable de donner le classement etc... A completer
    :param resultat:
    :return:
    """
    return 11.5