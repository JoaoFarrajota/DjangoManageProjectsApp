import django.urls
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path(r'profile/', views.profile, name='profile'),
    path(r'logout/', views.logout, name='logout'),
    path(r'welcome/', views.welcome, name='welcome'),
    path(r'createproject/', views.createproject, name='createproject'),
    path(r'projects/', views.projects, name='projects'), #All Projetos
    path(r'project/', views.project, name='project'), #Projeto individual


    path(r'deleteProject/', views.deleteProject, name='deleteProject'),
    path(r'createProject/', views.createProject, name='createProject'),

    path(r'deleteTarefa/', views.deleteTarefa, name='deleteTarefa'),
    path(r'createTarefa/', views.createTarefa, name='createTarefa'),
    path(r'updateTarefa/', views.updateTarefa, name='updateTarefa'),

    path(r'createAccount/', views.createAccount, name='createAccount'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
