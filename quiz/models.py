from django.db import models

# Create your models here.

class Profs(models.Model):
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    nom=models.CharField(max_length=30)

class Classes(models.Model):
    effectif = models.IntegerField()
    idProf=models.ForeignKey(Profs)
    nom=models.CharField(max_length=20)

class Quizz(models.Model):
    quizz=models.FileField(upload_to='quizzes/')
    correction=models.FileField(upload_to='corrections/')
    date = models.DateField(auto_now=True)
    idClasse=models.ForeignKey(Classes)
    idProf=models.ForeignKey(Profs)

class Eleves(models.Model):
    idClasse=models.ForeignKey(Classes)
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    nom=models.CharField(max_length=30)

class Resultats(models.Model):
    idQuizz=models.ForeignKey(Quizz)
    idEleve=models.ForeignKey(Eleves)
    resultat=models.FileField(upload_to='resultats/')


class Tags(models.Model):
    Tag = models.CharField(max_length= 20)

class QuizzToTag(models.Model):
    idTag = models.ForeignKey(Tags)
    idQuizz = models.ForeignKey(Quizz)