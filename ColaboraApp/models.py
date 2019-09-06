from django.db import models, connection

# Create your models here.
from django.db.models import Count


class Departamento(models.Model):
    nomeDepartamento = models.CharField(max_length=50, null = False, unique=True)

    class Meta:
        db_table = 'Departamento'

    def __str__(self):
        return self.nomeDepartamento


class Funcao(models.Model):
    nomeFuncao = models.CharField(max_length=20, null = False, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, to_field="nomeDepartamento")

    class Meta:
        db_table = 'Funcao'

    def __str__(self):
        return self.nomeFuncao

class Colaborador(models.Model):
    nome = models.CharField(max_length=60, null = False, unique=True)
    nascimento = models.DateField(null = False)
    rg = models.CharField(max_length=12, null = False)
    cpf = models.CharField(max_length=12, null = False)
    telefone = models.CharField(max_length=13, null = False)
    cnh = models.CharField(max_length=12, null = False)
    cnh_choices = (
        ('Não Possui', 'Não Possui'),
        ('A', 'A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('E','E')
    )

    cnh_tipo = models.CharField(max_length=12,choices=cnh_choices, default='Não Possui', null = False)

    sexo_choices = (
        ('M', 'M'),
        ('F', 'F'),
    )
    sexo_choices = models.CharField(max_length=2, choices=sexo_choices, null = False)

    departamento = models.ForeignKey(Departamento , on_delete=models.CASCADE, to_field='nomeDepartamento')

    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, to_field='nomeFuncao')

    foto_colaborador = models.BinaryField(max_length=None, editable=True)
	
    class Meta:
        db_table= 'Colaborador'

    def __str__(self):
        return self.nome


class TipoFormacao(models.Model):
    tipo_formacao = models.CharField(max_length=13, null = False, unique=True)

    class Meta:
        db_table = 'Tipo_Formacao'

    def __str__(self):
        return self.tipo_formacao


class Formacao(models.Model):
    colaborador = models.ForeignKey(Colaborador,on_delete=models.CASCADE, null = False)

    #tipo_choices = (
     #   ('Graduação','Graduação'),
     #   ('Pós-Graduação','Pós-Graduação'),
     #   ('Mestrado','Mestrado'),
     #   ('Doutorado','Doutorado'),
     #   ('Extensão','Extensão'),
     #   ('Certificação','Certificação')
   # )

    tipo_formacao = models.ForeignKey(TipoFormacao, on_delete=models.CASCADE, null = False, to_field='tipo_formacao')
    nome_curso = models.CharField(max_length=50, null = False)
    instituicao = models.CharField(max_length=50, null = False)
    dt_inicio = models.DateField(null = False)
    dt_termino = models.DateField(null = False)

    class Meta:
        db_table = 'Formacao'

    def __str__(self):
        return self.nome_curso


class HoraExtra(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null= False, to_field='nome')
    data = models.DateField(null=False)
    hora_inicio = models.TimeField(null=False)
    hora_fim = models.TimeField(null= False)
    faturado = models.BooleanField(null=False)


    class Meta:
        db_table = 'HoraExtra'

    def __str__(self):
        return self.colaborador

    # This method counts the extra hours that are still active, or be, those who aren´t invoiced
    def CountHoraExtraNaoFaturada(self, colaborador):

        with connection.cursor() as cursor:
            cursor.execute('select count(t.data) from public."HoraExtra" t where t.colaborador_id = '
                           '(select id from public."Colaborador" where nome = %s) and t.faturado = false', [colaborador])
            row = cursor.fetchone()
        return row[0]
    # This method limits the quantity of extra hours registered by week
