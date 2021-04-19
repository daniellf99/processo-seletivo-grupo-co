# Generated by Django 3.2 on 2021-04-19 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=9)),
                ('logradouro', models.CharField(max_length=200)),
                ('localidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recrutamento.candidato')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recrutamento.vaga')),
            ],
        ),
    ]
