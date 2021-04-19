# Django Vagas

Plataforma para gestão de recrutamento criada como parte de desafio para
processo seletivo do Grupo CO Empresas.

## Instalação

Após clonar o repositório, navegue para a pasta raiz do projeto (`djangoVagas/`)
e crie o ambiente python com `venv`:

`python3 -m venv venv`

No linux, ativamos o ambiente com:

`source venv/bin/activate`

Caso esteja no windows, veja [esta página](https://docs.python.org/pt-br/3/library/venv.html#creating-virtual-environments).

Para instalar todas as dependências, executamos:

`pip install -r requirements.txt`

Depois disso, preparamos o banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```

## Executando

Finalmente, podemos executar nosso servidor de desenvolvimento:

`python manage.py runserver`

Pronto! A página está disponível agora em http://127.0.0.1:8000/.