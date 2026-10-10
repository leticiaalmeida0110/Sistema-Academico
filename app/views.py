from django.shortcuts import render

# Create your views here.

from django.views import View
from .models import *


class PessoaView(View):
    def get(self, request, *args, **kwargs):
        dados = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'dados': dados})


class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        dados = Ocupacao.objects.all()
        return render(request, 'ocupacoes.html', {'dados': dados})


class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        dados = Instituicao.objects.all()
        return render(request, 'instituicoes.html', {'dados': dados})


class AreaView(View):
    def get(self, request, *args, **kwargs):
        dados = Area.objects.all()
        return render(request, 'areas.html', {'dados': dados})


class CursoView(View):
    def get(self, request, *args, **kwargs):
        dados = Curso.objects.all()
        return render(request, 'cursos.html', {'dados': dados})


class TurnoView(View):
    def get(self, request, *args, **kwargs):
        dados = GerenciarTurnos.objects.all()
        return render(request, 'turnos.html', {'dados': dados})


class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        dados = GerenciarDisciplinas.objects.all()
        return render(request, 'disciplinas.html', {'dados': dados})


class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        dados = GerenciarMatriculas.objects.all()
        return render(request, 'matriculas.html', {'dados': dados})


class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        dados = GerenciarAvaliacoes.objects.all()
        return render(request, 'avaliacoes.html', {'dados': dados})


class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        dados = GerenciarFrequencia.objects.all()
        return render(request, 'frequencias.html', {'dados': dados})


class TurmaView(View):
    def get(self, request, *args, **kwargs):
        dados = GerenciarTurmas.objects.all()
        return render(request, 'turmas.html', {'dados': dados})


class CidadeView(View):
    def get(self, request, *args, **kwargs):
        dados = Cidade.objects.all()
        return render(request, 'cidades.html', {'dados': dados})


class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        dados = GerenciarOcorrencias.objects.all()
        return render(request, 'ocorrencias.html', {'dados': dados})


class ManterDisciplinaView(View):
    def get(self, request, *args, **kwargs):
        dados = ManterDisciplinas.objects.all()
        return render(request, 'manter_disciplinas.html', {'dados': dados})


class TipoAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        dados = TipoAvaliacoes.objects.all()
        return render(request, 'tipos_avaliacoes.html', {'dados': dados})


class UFView(View):
    def get(self, request, *args, **kwargs):
        dados = UF.objects.all()
        return render(request, 'ufs.html', {'dados': dados})


class EstudanteView(View):
    def get(self, request, *args, **kwargs):
        dados = Estudantes.objects.all()
        return render(request, 'estudantes.html', {'dados': dados})


class ProfessorView(View):
    def get(self, request, *args, **kwargs):
        dados = Professor.objects.all()
        return render(request, 'professores.html', {'dados': dados})

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')