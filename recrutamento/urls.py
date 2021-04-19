from django.urls import path

from . import views

urlpatterns = [
    path('candidatos/<int:id_candidato>/editar/', views.editar_candidato),
    path('candidatos/<int:id_candidato>/excluir/', views.remover_candidato),
    path('candidatos/adicionar/', views.adicionar_candidato),
    path('candidatos/', views.candidatos),
    path('vagas/<int:id_vaga>/editar/', views.editar_vaga),
    path('vagas/<int:id_vaga>/excluir/', views.remover_vaga),
    path('vagas/adicionar/', views.adicionar_vaga),
    path('vagas/', views.vagas),
    path('', views.index),
]