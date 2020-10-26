from django.db import models

# Create your models here.

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=32,unique=True)
    Nome = models.CharField(max_length=9999)
    email = models.CharField(max_length=9999)
    password = models.CharField(max_length=64)
    class Meta:
        db_table = 'Users'

class Projetos(models.Model):
    ID_Projeto = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=9999)
    horacomecada = models.DateTimeField()
    horafinalizada = models.DateTimeField()
    class Meta:
        db_table = 'Projetos'

class Membros_Grupos(models.Model):
    AddID = models.AutoField(primary_key=True)
    ID_Projeto = models.IntegerField()
    UserID = models.IntegerField()
    #ID_Projeto = models.ForeignKey(Projetos, on_delete = models.CASCADE)
    class Meta:
        managed = False
        db_table = 'Membros_Grupos'
        unique_together = (("ID_Projeto","UserID"),)

class Tarefas(models.Model):
    TarefaID = models.AutoField(primary_key=True)
    Nome = models.TextField()
    horacomecada = models.DateTimeField()
    horafinalizada = models.DateTimeField()
    UserID = models.IntegerField()
    ID_Projeto = models.IntegerField()
    #UserID = models.ForeignKey(Users, on_delete = models.CASCADE)
    #ID_Projeto = models.ForeignKey(Projetos, on_delete = models.CASCADE)
    class Meta:
        db_table = 'Tarefas'
