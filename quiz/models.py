from django.db import models

# Create your models here.

class Profs(models.Model):
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    nom=models.CharField(max_length=30)


class Quizz(models.Model):
    quizz=models.URLField()
    correction=models.URLField()
    date = models.DateField()

class Classes(models.Model):
    effectif = models.IntegerField()
    idProf=models.ForeignKey(Profs)
    nom=models.CharField(max_length=20)

class Eleves(models.Model):
    idClasse=models.ForeignKey(Classes)
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    nom=models.CharField(max_length=30)

class Resultats(models.Model):
    idQuizz=models.ForeignKey(Quizz)
    idEleve=models.ForeignKey(Eleves)
    resultat=models.URLField()

class Tags(models.Model):
    Tag = models.CharField(max_length= 20)

class QuizzToTag(models.Model):
    idTag = models.ForeignKey(Tags)
    idQuizz = models.ForeignKey(Quizz)