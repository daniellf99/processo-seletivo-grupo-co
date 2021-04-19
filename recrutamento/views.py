from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from . import services
from .forms import VagaForm, CandidatoForm


def index(request):
    return redirect('/vagas/')


# Vagas
def vagas(request):
    return render(request, 'recrutamento/vagas.html', {
        "vagas": services.listar_vagas()
    })


def editar_vaga(request, id_vaga: int):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            cargo = form.cleaned_data['cargo']
            descricao = form.cleaned_data['descricao']
            services.editar_vaga(id_vaga, cargo, descricao)
            return HttpResponseRedirect('/vagas/')
    else:
        vaga = services.listar_vaga(id_vaga)
        dados_form = {
            "cargo": vaga.cargo,
            "descricao": vaga.descricao
        }
        return render(request, 'recrutamento/editarVaga.html', {
            "form": VagaForm(initial=dados_form)
        })


def adicionar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            cargo = form.cleaned_data['cargo']
            descricao = form.cleaned_data['descricao']
            services.adicionar_vaga(cargo, descricao)
            return HttpResponseRedirect('/vagas/')
    else:
        return render(request, 'recrutamento/adicionarVaga.html', {
            "form": VagaForm()
        })


def remover_vaga(request, id_vaga: int):
    services.remover_vaga(id_vaga)
    return HttpResponseRedirect('/vagas/')


# Candidatos
def candidatos(request):
    return render(request, 'recrutamento/candidatos.html', {
        "candidatos": services.listar_candidatos(),
    })


def editar_candidato(request, id_candidato: int):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cep = form.cleaned_data['cep']
            services.editar_candidato(id_candidato, nome, cep)
            return HttpResponseRedirect('/candidatos/')
    else:
        candidato = services.listar_candidato(id_candidato)
        dados_form = {
            "nome": candidato.nome,
            "cep": candidato.cep
        }
        return render(request, 'recrutamento/editarCandidato.html', {
            "form": CandidatoForm(initial=dados_form)
        })


def adicionar_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cep = form.cleaned_data['cep']
            services.adicionar_candidato(nome, cep)
            return HttpResponseRedirect('/candidatos/')
    else:
        return render(request, 'recrutamento/adicionarCandidato.html', {
            "form": CandidatoForm()
        })


def remover_candidato(request, id_candidato: int):
    services.remover_candidato(id_candidato)
    return HttpResponseRedirect('/candidatos/')
