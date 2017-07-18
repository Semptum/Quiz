from django.db import models

# Create your models here.

class Eleves(models.Model):
    idClasse=models.ForeignKey("Classes")
    password=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    nom=models.CharField(max_length=30)

class Quiz(models.Model):
    idProf=models.ForeignKey("Profs")
    quiz=models.URLField()
    reponse=models.URLField()

class Profs(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)

class Classes(models.Model):
    idProf=models.ForeignKey("Profs")
    identifiant=models.CharField(max_length=20)

class Resultats(models.Model):
    idQuiz=models.ForeignKey(Quiz)
    idEleve=models.ForeignKey(Eleves)
    resultat=models.URLField()
