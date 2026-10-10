from django.db import models

# Create your models here.


class UF(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do estado")
    sigla = models.CharField(max_length=2, verbose_name="Sigla")

    def __str__(self):
        return self.sigla

    class Meta:
        verbose_name = "UF"
        verbose_name_plural = "UFs"

class Cidade(models.Model):
    nome=models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf=models.ForeignKey( UF, on_delete=models.CASCADE, verbose_name="UF")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome=models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome das pessoas") # verbose_name: como vai aparecer para o usuário
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length = 11, verbose_name="cpf")
    data_nasc= models.DateField(verbose_name="Data de nascimento")
    email=models.CharField(max_length=100, verbose_name="email")
    cidade=models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao=models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")
    turma = models.ForeignKey("GerenciarTurmas", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Turma")

    def __str__(self):
            return self.nome
    
    class Meta:
            verbose_name = "Nome"
            verbose_name_plural = "Nomes"

class Estudantes(Pessoa):
        matricula = models.CharField(max_length=20)

class Professor(Pessoa):
        especialidade = models.CharField(max_length=100)

class Instituicao(models.Model):
    nome=models.CharField(max_length=100,  verbose_name="Nome da Instituição")
    site=models.CharField(max_length=100, verbose_name="Site")
    email=models.CharField(max_length=100, verbose_name="Email")
    telefone=models.CharField(max_length=100, verbose_name="Telefone")
    cidade=models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class Area(models.Model):
    nome=models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

class Curso(models.Model):
    nome=models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total=models.CharField(max_length=100, verbose_name="Carga horária")
    duracao_meses=models.IntegerField(verbose_name="Duração de meses")
    area=models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area")
    instituicao=models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class GerenciarTurnos(models.Model):
    nome=models.CharField(max_length=100, verbose_name="Turno")

#class Area(models.Model):
    #cincias_exatas=models.CharField(max_lenght=100, verbose_name="Ciências Exatas")
    #portugues=models.CharField(max_lenght=100, verbose_name="Português")
    #biologia=models.CharField(max_lenght=100, verbose_name="Biologia")
    #historia=models.CharField(max_lenght=100, verbose_name="História")
    #programacao=models.CharField(max_lenght=100, verbose_name="Programação")


class GerenciarDisciplinas(models.Model):
    nome=models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area=models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class GerenciarMatriculas(models.Model):
    data_inicio=models.DateField(verbose_name="Data de início")
    data_previsao_termino=models.DateField(verbose_name="Data de previsão de término")
    instituicao=models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

class TipoAvaliacoes(models.Model):
    nome=models.CharField(max_length=100, verbose_name="Tipo de avaliação")

    def __str__(self):
            return self.nome
    
    class Meta:
            verbose_name = "Nome"
            verbose_name_plural = "Nomes"

class GerenciarAvaliacoes(models.Model):
    descricao=models.CharField(max_length=100, verbose_name="Descrição")
    nota=models.DecimalField(max_digits=5, decimal_places=2)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina=models.ForeignKey(GerenciarDisciplinas, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    tipo_avaliacao=models.ForeignKey(TipoAvaliacoes, on_delete=models.CASCADE, verbose_name="Tipo de avaliações")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class GerenciarFrequencia(models.Model):
    numero_faltas=models.IntegerField(verbose_name="Número de faltas")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina=models.ForeignKey(GerenciarDisciplinas, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa", related_name="frequencias_pessoa")
    estudante = models.ForeignKey("Estudantes", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Estudante", related_name="frequencias_estudante")

class GerenciarTurmas(models.Model):
    nome=models.CharField(max_length=100, verbose_name="Nome da Turma")
    turno=models.ForeignKey(GerenciarTurnos, on_delete=models.CASCADE, verbose_name="Turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
    
class GerenciarOcorrencias(models.Model):
    descricao=models.CharField(max_length=100, verbose_name="Descrição")
    data=models.DateField(verbose_name="Data da Ocorrência")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina=models.ForeignKey(GerenciarDisciplinas, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

class ManterDisciplinas(models.Model):
    carga_horaria=models.IntegerField(verbose_name="Carga Horária")
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina=models.ForeignKey(GerenciarDisciplinas, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    turno=models.ForeignKey(GerenciarTurnos, on_delete=models.CASCADE, verbose_name="Turno")

