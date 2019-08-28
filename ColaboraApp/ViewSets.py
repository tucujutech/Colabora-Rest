from rest_framework.viewsets import ModelViewSet

from .Serializers import *
from .models import *

# =========== Colaborador ViewSet ========


class ColaboradorViewSet(ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer


# ========== Formacao ViewSet ==============


class FormacaoViewSet(ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer


# ========== Tipo Formacao ViewSet =========

class TipoFormacaoViewSet(ModelViewSet):
    queryset = TipoFormacao.objects.all()
    serializer_class = TipoFormacaoSerializer


# ========== Departamento ViewSet ==========

class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


# =========== Funcao ViewSet ================

class FuncaoViewSet(ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer