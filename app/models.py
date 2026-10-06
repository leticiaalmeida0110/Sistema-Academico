from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome da Cidade")
    uf=models.CharField(max_lenght=2, verbose_name="UF")

class Ocupacao(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome")

class GerenciarPessoas(models.Model):
    nome = models.CharField(max_lenght=100, verbose_name="Nome das pessoas") # verbose_name: como vai aparecer para o usuário
    nome_do_pai = models.CharField(max_lenght=100, verbose_name="Nome do pai")
    nome_da_mae = models.CharField(max_lenght=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_lenght = 100, verbose_name="cpf")
    data_nasc= models.CharField(max_lenght=100, verbose_name="Data de nascimento")
    email=models.CharField(max_lenght=100, verbose_name="email")
    cidade=models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao=models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

class InstituicaoDeEnsino(models.Model):
    nome=models.CharField(max_lenght=100,  verbose_name="Nome do site")
    site=models.CharField(max_lenght=100, verbose_name="Site")
    email=models.CharField(max_lenght=100, verbose_name="Email")
    telefone=models.CharField(max_lenght=100, verbose_name="Telefone")
    cidade=models.CharField(max_lenght=100, verbose_name="Cidade")

class GerenciarAreasDoSaber(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome")

class GerenciarCursos(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome do Curso")
    carga_horaria=models.CharField(max_lenght=100, verbose_name="Carga horária")