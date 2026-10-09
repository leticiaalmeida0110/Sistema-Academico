from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome da Cidade")
    uf=models.CharField(max_lenght=2, verbose_name="UF")

class Ocupacao(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome")

class Pessoa(models.Model):
    nome = models.CharField(max_lenght=100, verbose_name="Nome das pessoas") # verbose_name: como vai aparecer para o usuário
    nome_do_pai = models.CharField(max_lenght=100, verbose_name="Nome do pai")
    nome_da_mae = models.CharField(max_lenght=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_lenght = 100, verbose_name="cpf")
    data_nasc= models.CharField(max_lenght=100, verbose_name="Data de nascimento")
    email=models.CharField(max_lenght=100, verbose_name="email")
    cidade=models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao=models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

class Instituicao(models.Model):
    nome=models.CharField(max_lenght=100,  verbose_name="Nome da Instituição")
    site=models.CharField(max_lenght=100, verbose_name="Site")
    email=models.CharField(max_lenght=100, verbose_name="Email")
    telefone=models.CharField(max_lenght=100, verbose_name="Telefone")
    cidade=models.CharField(max_lenght=100, verbose_name="Cidade")

class Area(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome")

class Curso(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome do Curso")
    carga_horaria_total=models.CharField(max_lenght=100, verbose_name="Carga horária")
    duracao_meses=models.CharField(max_lenght=100, verbose_name="Duração de meses")
    area=models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area")
    instituicao=models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")

class GerenciarTurnos(models.Model):
    matutino=models.CharField(max_lenght=100, verbose_name="Turno matutino")
    noturno=models.CharField(max_lenght=100, verbose_name="Turno noturno")

#class Area(models.Model):
    #cincias_exatas=models.CharField(max_lenght=100, verbose_name="Ciências Exatas")
    #portugues=models.CharField(max_lenght=100, verbose_name="Português")
    #biologia=models.CharField(max_lenght=100, verbose_name="Biologia")
    #historia=models.CharField(max_lenght=100, verbose_name="História")
    #programacao=models.CharField(max_lenght=100, verbose_name="Programação")


class GerenciarDisciplinas(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome da disciplina")
    area=models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area")

class GerenciarMatriculas(models.Model):
    data_inicio=models.CharField(max_lenght=100, verbose_name="Data de início")
    data_previsao_termino=models.CharField(max_lenght=100, verbose_name="Data de previsão de término")
    instituicao=models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

class TipoAvaliacoes(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Tipo de avaliação")

class GerenciarAvaliacoes(models.Model):
    descricao=models.CharField(max_lenght=100, verbose_name="Descrição")
    nota=models.CharField(max_lenght=100, verbose_name="Nota")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina=models.ForeignKey(GerenciarDisciplinas, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    tipo_avaliacao=models.ForeignKey(TipoAvaliacoes, on_delete=models.CASCADE, verbose_name="Tipo de avaliações")

class GerenciarFrequencia(models.Model):
    numero_faltas=models.CharField(max_lenght=100, verbose_name="Número de faltas")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina=models.ForeignKey(GerenciarDisciplinas, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

class GerenciarTurmas(models.Model):
    nome=models.CharField(max_lenght=100, verbose_name="Nome da Turma")
    turno=models.ForeignKey(GerenciarTurnos, on_delete=models.CASCADE, vebose_name="Turno")

class GerenciarOcorrencias(models.Model):
    descricao=models.CharField(max_lenght=100, verbose_name="Descrição")
    data=models.CharField(max_lenght=8, verbose_name="Data da Ocorrência")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina=models.ForeignKey(GerenciarDisciplinas, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

class ManterDisciplinas(models.Model):
    carga_horaria=models.CharField(max_lenght=100, verbose_name="Carga Horária")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina=models.ForeignKey(GerenciarDisciplinas, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    turno=models.ForeignKey(GerenciarTurnos, on_delete=models.CASCADE, vebose_name="Turno")

