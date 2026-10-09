from django.contrib import admin

# Register your models here.
from.models import *
from django.contrib import admin

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(Instituicao)
admin.site.register(Curso)
admin.site.register(GerenciarTurnos)
admin.site.register(Area)
admin.site.register(GerenciarDisciplinas)
admin.site.register(GerenciarMatriculas)
admin.site.register(GerenciarAvaliacoes)
admin.site.register(GerenciarFrequencia)
admin.site.register(GerenciarTurmas)
admin.site.register(GerenciarOcorrencias)
admin.site.register(ManterDisciplinas)
admin.site.register(TipoAvaliacoes)