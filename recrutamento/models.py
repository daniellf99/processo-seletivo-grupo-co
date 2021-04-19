from django.db import models


class Vaga(models.Model):
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=200)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)


class Inscricao(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
