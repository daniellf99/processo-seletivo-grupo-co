from django import forms


class VagaForm(forms.Form):
    cargo = forms.CharField(label='Nome do cargo', max_length=100)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea)


class CandidatoForm(forms.Form):
    nome = forms.CharField(label='Nome do candidato', max_length=100)
    cep = forms.CharField(label='CEP', max_length=9)
