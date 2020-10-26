from django.shortcuts import render
import sqlite3
from sqlite3 import Error
from os import path
from polls.models import *
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
import json
import datetime

# Create your views here.

from django.http import HttpResponse


def create_db(db_file):
    conn = sqlite3.connect(db_file)

    #conn.cursor().execute('DROP TABLE Users')
    #conn.cursor().execute('DROP TABLE Projetos')
    #conn.cursor().execute('DROP TABLE Membros_Grupos')
    #conn.cursor().execute('DROP TABLE Tarefas')

    sql_create_users_table =  '''CREATE TABLE IF NOT EXISTS Users(
                                        UserID INTEGER PRIMARY KEY,
                                    	Username VARCHAR(32) UNIQUE,
                                    	Nome Completo MEDIUMTEXT,
                                        email MEDIUMTEXT,
                                    	password VARCHAR(64)
                                )
                                '''
    conn.cursor().execute(sql_create_users_table)

    sql_create_projetos_table =  '''CREATE TABLE IF NOT EXISTS Projetos(
                                    ID_Projeto INTEGER PRIMARY KEY,
                                    Nome MEDIUMTEXT,
                                    horacomecada DATETIME,
                                    horafinalizada DATETIME

                                )
                                '''
    conn.cursor().execute(sql_create_projetos_table)

    sql_create_membrosdogrupo_table =  '''CREATE TABLE IF NOT EXISTS Membros_Grupos(
                                    AddID INTEGER PRIMARY KEY,
                                    ID_Projeto int,
                                    UserID int,
                                    FOREIGN KEY (ID_Projeto) REFERENCES Projetos(ID_Projeto)
                                )
                                '''
    conn.cursor().execute(sql_create_membrosdogrupo_table)

    sql_create_tarefas_table =  '''CREATE TABLE IF NOT EXISTS Tarefas(
                                    TarefaID INTEGER PRIMARY KEY,
                                    Nome TEXT,
                                    horacomecada DATETIME,
                                    horafinalizada DATETIME,
                                    UserID int,
                                    ID_Projeto int(11)
                                )'''
    c = conn.cursor().execute(sql_create_tarefas_table)


def create_connection(db_file,list):
    """ create a database connection to a SQLite database """
    conn = None

    try:
        conn = sqlite3.connect(db_file)

        return Utilizador.Nome

    except Error as e:
        return e
    finally:
        if conn:
            conn.close()

def getUser(id):
    return Users.objects.get(UserID=id) #by ID

def getUserbyUser(User):
    return Users.objects.get(Username=User) #by ID

def getAllUsers():
    return Users.objects.all() #by ID

def createUser(list):
    if(list[0]!=None):
        Users.objects.create(Username=list[0],Nome=list[1],email=list[2],password=list[3])
        return "sucess"
    else:
        return "Erro"

def checkUser(list):
    return Users.objects.get(Username=list[0],password=list[1])

def deleteUser(id):
    Users.objects.get(UserID=id).delete()
    return "sucess"

def updateUser(list):
    Utilizador = Users.objects.get(UserID=list[0])
    Utilizador.Username = list[1]
    Utilizador.Nome = list[2]
    #Utilizador.email = list[3]
    Utilizador.password = list[4]
    Utilizador.Permissoes = list[5]
    return "sucess"

def getProjetos(list):
    return Projetos.objects.get(ID_Projeto=list[0]) #by ID

def getAllProjetos():
    return Projetos.objects.all()

def createProjetos(list):
    Projeto = Projetos.objects.create(Nome=list[0],horacomecada=list[1],horafinalizada=list[2])
    return Projeto

def deleteProjetos(list):
    return Projetos.objects.get(ID_Projeto=list[0]).delete()
    return "sucess"

def deleteTarefasdeProjetos(list):
    Tarefas.objects.filter(ID_Projeto=list[0]).delete()
    return "sucess"

def updateProjetos(list):
    Projeto = Projetos.objects.get(ID_Projeto=list[0])
    Projeto.horacomecada = list[2]
    Projeto.horafinalizada = list[3]
    Projeto.save()
    return "sucess"

def updateNomeProjeto(list):
    Projeto = Projetos.objects.get(ID_Projeto=list[0])
    Projeto.Nome = list[1]
    Projeto.save()

def getMembros_Grupos(list):
    return Membros_Grupos.objects.filter(UserID=list[0])

def createMembros_Grupos(list):
    #Adicionar ,Permissao=list[2]
    Membros_Grupos.objects.create(ID_Projeto=list[0],UserID=list[1])
    return "sucess"

def deleteMembros_Grupos(list):
    Membros_Grupos.objects.get(ID_Projeto=list[0],UserID=list[1]).delete()
    return "sucess"

def getTarefas(list):
    return Tarefas.objects.filter(ID_Projeto=list[0]) #by ID

def getTarefaByID(list):
    return Tarefas.objects.filter(TarefaID=list[0],ID_Projeto=list[1]) #by ID

def createTarefas(list):
    Tarefa = Tarefas.objects.create(Nome=list[0],horacomecada=list[1],horafinalizada=list[2],UserID=list[3],ID_Projeto=list[4])
    return Tarefa

def deleteTarefas(list):
    Tarefas.objects.get(TarefaID=list[0],ID_Projeto=list[1]).delete()
    return "sucess"

def updateTarefas(list):
    Tarefa = Tarefas.objects.get(TarefaID=list[0],ID_Projeto=list[4])
    Tarefa.Nome = list[1]
    Tarefa.horacomecada = list[2]
    Tarefa.horafinalizada = list[3]
    Tarefa.save()
    return "sucess"

@csrf_exempt
def index(request):
    create_db("D:\Transferências\mysite 18-10 v2\mysite\db.sqlite3")

    if request.method == 'POST':
        list = [request.POST.get('username'),request.POST.get('pass')]
        #print(list)
        #return HttpResponse(getUser(46).Username+getUser(46).password)
        try:
            user = checkUser(list)
            request.session['UserID'] = user.UserID;
            request.session['Username'] = user.Username;
            request.session['Nome'] = user.Nome;
            return redirect('/welcome')
        except:
            return redirect("/")
    else:
        if(request.session.is_empty()):
            #request.GET.get("wrongpassword")
            context = {
            #'wrongpassord': "Password incorrecta"
            }
            return render(request, 'home.html', context=context)
        else:
            context = {}
            return redirect('/welcome')
        #username = request.GET.get('Username')

@csrf_exempt
def welcome(request):
    context = {
    }
    if(request.session.is_empty()):
        return redirect('/')
    else:
        return render(request, 'welcome.html', context=context)

@csrf_exempt
def logout(request):
    request.session.flush()
    return redirect('/')

@csrf_exempt
def profile(request):
    if(request.session.is_empty()):
        context = {}
        return render(request, 'home.html', context=context)
    else:
        projs = []
        for proj in getMembros_Grupos([request.session['UserID']]):
            projs.append(getProjetos([proj.ID_Projeto]))
        context = {
            'Username': request.session['Username'],
            'Nome': request.session['Nome'],
            'projects': projs,
        }
        return render(request, 'profile.html', context=context)

@csrf_exempt
def projects(request):
    if(request.session.is_empty()):
        return redirect('/')
    else:
        projs = []
        for proj in getMembros_Grupos([request.session['UserID']]):
            projs.append(getProjetos([proj.ID_Projeto]))
        context = {
            'projects': projs,
        }
        return render(request, 'consultarProjetos.html', context=context)

@csrf_exempt
def createproject(request):
    if(request.session.is_empty()):
        return redirect('/')
    else:
        context = {
            #'tasks': getTarefas([1])
        }
        print(getAllProjetos())
        if request.method == 'POST':
            list = [1,request.POST.get("nome"),'2020-10-16 10:00:00','2020-10-17 10:00:00']
            ID_Projeto = createProjetos(list)
            createMembros_Grupos([ID_Projeto,request.session['UserID'],'user'])
            return redirect('/project/?ID_Projeto='+str(ID_Projeto))
        else:
            return render(request, 'createproject.html', context=context)

@csrf_exempt
def project(request):
    if(request.session.is_empty()):
        return redirect('/')
    else:
        context = {
            'project': getProjetos([request.GET.get("ID_Projeto")]),
            'tasks': getTarefas([request.GET.get("ID_Projeto")]),
            'user': request.session['Username']
        }


        return render(request, 'editproject.html', context=context)




@csrf_exempt
def deleteProject(request):
    deleteMembros_Grupos([request.GET.get('ID_Projeto'),request.session['UserID']])
    deleteProjetos([request.GET.get('ID_Projeto')])
    deleteTarefasdeProjetos([request.GET.get('ID_Projeto')])
    return HttpResponse("sucess")

@csrf_exempt
def createProject(request):
    ret = createProjetos([request.POST.get('Nome'),'2020-10-17 10:00:00','2020-10-18 10:00:00'])
    createMembros_Grupos([ret.ID_Projeto, request.session['UserID']])
    print(ret.horacomecada)
    return HttpResponse(ret.ID_Projeto)

@csrf_exempt
def deleteTarefa(request):
    deleteTarefas([request.GET.get('TarefaID'),request.GET.get('ID_Projeto')])
    return HttpResponse("sucess")

@csrf_exempt
def createTarefa(request):
    ret = createTarefas(["New Tarefa",'2020-10-17 10:00:00','2020-10-17 10:00:00',request.session['UserID'],request.POST.get('ID_Projeto')])
    #return HttpResponse(["New Tarefa",'2020-10-17','2020-10-18',request.session['UserID'],request.POST.get('ID_Projeto')])
    return HttpResponse(ret.TarefaID)

@csrf_exempt
def updateTarefa(request):
    y = json.loads(request.POST.get('json'))
    id_projeto = request.POST.get('id_projeto')
    nomeprojeto = request.POST.get('nomeprojeto')

    for e in y:
        if e != None:
            #updateTarefas([e['tarefa_id'],e['0'],e['1'],e['2'],id_projeto])
            updateTarefas([e['tarefa_id'],e['0'],e['1'],e['2'],id_projeto])
            Projeto = getProjetos([id_projeto])
            Projeto.Nome = nomeprojeto
            Projeto.save()
            print(e['1'])
            print(e['2'])

    return HttpResponse("aa");

@csrf_exempt
def createAccount(request):
    createUser([request.POST.get('Username'),request.POST.get('Nome'),request.POST.get('email'),request.POST.get('password')])
    return HttpResponse("sucess")
