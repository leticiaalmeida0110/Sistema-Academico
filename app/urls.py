
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoaView.as_view(), name='pessoas'),
    path('ocupacoes/', OcupacaoView.as_view(), name='ocupacoes'),
    path('instituicoes/', InstituicaoView.as_view(), name='instituicoes'),
    path('areas/', AreaView.as_view(), name='areas'),
    path('cursos/', CursoView.as_view(), name='cursos'),
    path('turnos/', TurnoView.as_view(), name='turnos'),
    path('disciplinas/', DisciplinaView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculaView.as_view(), name='matriculas'),
    path('avaliacoes/', AvaliacaoView.as_view(), name='avaliacoes'),
    path('frequencias/', FrequenciaView.as_view(), name='frequencias'),
    path('turmas/', TurmaView.as_view(), name='turmas'),
    path('cidades/', CidadeView.as_view(), name='cidades'),
    path('ocorrencias/', OcorrenciaView.as_view(), name='ocorrencias'),
    path('manter-disciplinas/', ManterDisciplinaView.as_view(), name='manter_disciplinas'),
    path('tipos-avaliacoes/', TipoAvaliacaoView.as_view(), name='tipos_avaliacoes'),
    path('ufs/', UFView.as_view(), name='ufs'),
    path('estudantes/', EstudanteView.as_view(), name='estudantes'),
    path('professores/', ProfessorView.as_view(), name='professores'),
]