from rest_framework.serializers import ModelSerializer

from .models import *

# ===== Colaborador Serializer ==========


class ColaboradorSerializer(ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ('id', 'nome', 'nascimento', 'rg', 'cpf',
                  'telefone', 'cnh', 'cnh_tipo', 'sexo_choices',
                  'departamento', 'funcao', 'foto_colaborador')


# ===== Formacao Serializer =============


class FormacaoSerializer(ModelSerializer):
    class Meta:
        model = Formacao
        fields = ('id', 'colaborador', 'tipo_formacao', 'nome_curso', 'instituicao',
                  'dt_inicio', 'dt_termino')


# ===== Tipo Formacao Serializer ==========


class TipoFormacaoSerializer(ModelSerializer):
    class Meta:
        model = TipoFormacao
        fields = ('id', 'tipo_formacao')


# ===== Departamento Serializer ============


class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nomeDepartamento')


# ===== Funcao Serializer =================


class FuncaoSerializer(ModelSerializer):
    class Meta:
        model = Funcao
        fields = ('id', 'nomeFuncao', 'departamento')


# ========= Hora Extra Serializer ================
class HoraExtraSerializer(ModelSerializer):
    class Meta:
        model =HoraExtra
        fields = ('id', 'colaborador', 'data', 'hora_inicio', 'hora_fim', 'faturado')
