from typing import List
import requests

from .models import Vaga, Inscricao, Candidato


# Candidatos
def listar_candidatos() -> List[Candidato]:
    return Candidato.objects.all()


def listar_candidato(id_candidato: int) -> Candidato:
    return Candidato.objects.get(pk=id_candidato)


def adicionar_candidato(nome: str, cep: str) -> None:
    endereco = _consultar_cep(cep)
    candidato = Candidato(nome=nome, cep=endereco['cep'], localidade=endereco['localidade'],
                          uf=endereco['uf'], logradouro=endereco['logradouro'])
    candidato.save()


def editar_candidato(id_candidato: int, nome: str, cep: str) -> None:
    candidato = Candidato.objects.get(pk=id_candidato)
    if not candidato:
        raise Exception("ID de candidato não corresponde a um registro válido.")

    candidato.nome = nome
    endereco = _consultar_cep(cep)
    candidato.cep = endereco['cep']
    candidato.localidade = endereco['localidade']
    candidato.logradouro = endereco['logradouro']
    candidato.uf = endereco['uf']
    candidato.save()


def remover_candidato(id_candidato: int) -> None:
    candidato = Candidato.objects.get(pk=id_candidato)
    if candidato:
        candidato.delete()


# Vagas
def listar_vagas() -> List[Vaga]:
    return Vaga.objects.all()


def listar_vaga(id_vaga: int) -> Vaga:
    return Vaga.objects.get(pk=id_vaga)


def adicionar_vaga(cargo: str, descricao: str) -> None:
    vaga = Vaga(cargo=cargo, descricao=descricao)
    vaga.save()


def editar_vaga(id_vaga: int, cargo: str, descricao: str) -> None:
    vaga = Vaga.objects.get(pk=id_vaga)
    if not vaga:
        raise Exception("ID de vaga não corresponde a um registro válido.")

    vaga.cargo = cargo
    vaga.descricao = descricao
    vaga.save()


def inscrever_candidato(id_candidato: int, id_vaga: int) -> None:
    candidato = Candidato.objects.get(pk=id_candidato)
    if not candidato:
        raise Exception("ID de candidato não corresponde a um registro válido.")

    vaga = Vaga.objects.get(pk=id_vaga)
    if not vaga:
        raise Exception("ID de vaga não corresponde a um registro válido.")

    Inscricao(candidato=candidato, vaga=vaga).save()


def remover_vaga(id_vaga: int) -> None:
    vaga = Vaga.objects.get(pk=id_vaga)
    if vaga:
        vaga.delete()


# utils
def _consultar_cep(cep: str):
    digitos_cep = cep.replace('-', '')
    url = f'https://viacep.com.br/ws/{digitos_cep}/json'
    resposta = requests.get(url)
    if resposta.status_code != 200:
        return None
    else:
        return resposta.json()
