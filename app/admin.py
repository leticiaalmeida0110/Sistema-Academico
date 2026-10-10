from django.contrib import admin

# Register your models here.
from.models import *

from .models import Ocupacao, Pessoa
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1


@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

# ii) Instituição e cursos
class CursoInstituicaoInline(admin.TabularInline):
    model = Curso
    extra = 1


@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInstituicaoInline]


# iii) Área do saber e cursos
class CursoAreaInline(admin.TabularInline):
    model = Curso
    extra = 1


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    inlines = [CursoAreaInline]


# iv) Cursos e disciplinas
class DisciplinaInline(admin.TabularInline):
    model = ManterDisciplinas
    extra = 1


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [DisciplinaInline]


# v) Disciplinas e avaliações
class AvaliacaoInline(admin.TabularInline):
    model = GerenciarAvaliacoes
    extra = 1


@admin.register(GerenciarDisciplinas)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

class PessoaTurmaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

@admin.register(GerenciarTurmas)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [PessoaTurmaInline]


admin.site.register(Cidade)
admin.site.register(GerenciarTurnos)
admin.site.register(GerenciarMatriculas)
admin.site.register(GerenciarFrequencia)
admin.site.register(GerenciarOcorrencias)
admin.site.register(ManterDisciplinas)
admin.site.register(TipoAvaliacoes)