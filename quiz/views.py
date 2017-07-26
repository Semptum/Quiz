from django.shortcuts import render, redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from quiz.models import *

def msg(request,message):
    return render(request,'quiz/message.html',{'msg':message})


# Create your views here.
def index(request):
    if request.session.has_key('username'):
        return dashboard(request)
    return render(request, 'quiz/index.html', {})

def available(request):
    if not request.session.has_key('username'):
        return render(request, 'quiz/index.html', {})
    status=request.session['status']
    if status=="prof":
        prof=Profs.objects.get(username=request.session['username'])
        QuizzsExistants=Quizz.objects.filter(idProf=prof)
        L=[]
        for q in QuizzsExistants:
            classe=q.idClasse.nom
            date=q.idClasse.date
            url=q.idClasse.quizz
            corr=q.idClasse.correction
            L+=["Quizz posé le "+str(date)+" a la classe "+classe+": "+url+" . Correction: "+corr]
        return render(request,'quiz/quizzes.html',{'quizzes':L})
    eleve=Eleves.objects.filter(username=request.session['username'])[0]
    classe=eleve.idClasse
    QuizzsExistants=list(Quizz.objects.filter(idClasse=classe))
    L = []
    for q in QuizzsExistants:
        classe = q.idClasse.nom
        date = q.idClasse.date
        url = q.idClasse.quizz
        corr = q.idClasse.correction
        L += ["Quizz posé le " + str(date) + " a la classe " + classe + ": " + url + " . Correction: " + corr]
    return render(request, 'quiz/available.html', {'quizzes': L})

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
    eleves=list(Eleves.objects.filter(username=user))
    profs=list(Profs.objects.filter(username=user))
    print(profs)
    if len(eleves)!=0 and len(profs)==0:
        u=eleves[0]
        status="eleve"
    elif len(eleves)==0 and len(profs)!=0:
        u=profs[0]
        status="prof"
    else:
        return msg(request,"Compte inexistant")
    hashed=u.password
    correct=pbkdf2_sha256.verify(pswd,hashed)
    if correct:
        request.session['username']=user
        request.session['status']=status
        return redirect(dashboard)
    return msg(request,"Mauvais mot de passe")

def logout(request):
    try:
        del request.session['username']
        del request.session['status']
    except:
        pass
    return render(request,'quiz/message.html')

def signup(request):
    if request.POST=={}:
        L = Classes.objects.raw("SELECT id,Nom FROM quiz_classes")
        Noms = [i.Nom for i in L]
        return render(request, 'quiz/signup.html', {"noms":Noms})
    user=request.POST['username']
    pswd=request.POST['password']
    nom = request.POST['last name']
    prenom =request.POST['first name']
    statut = request.POST['statut']
    if statut=="Eleve":
        classe = request.POST['classe']
    deja=list(Profs.objects.filter(username=user))+list(Eleves.objects.filter(username=user))
    if deja!=[]:
        return render(request,'quiz/erreur.html',{'error':"Utilisateur deja existant"})
    hashed=pbkdf2_sha256.encrypt(pswd, rounds=200000, salt_size=16)
    if statut == "Eleve":
        t = Classes.objects.filter(nom = classe)
        eleve = Eleves(nom = nom, prenom = prenom, password = hashed, username = user, idClasse = t[0] )
        eleve.save()
    else :
        prof = Profs(nom = nom, prenom = prenom, password = hashed, username = user)
        prof.save()
    text = "Merci de votre inscription. Vous allez recevoir un email de confirmation vous permettant d'activer votre compte."
    return msg(request,text)