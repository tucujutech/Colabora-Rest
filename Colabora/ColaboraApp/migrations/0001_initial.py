# Generated by Django 2.2 on 2019-08-28 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('nascimento', models.DateField()),
                ('rg', models.CharField(max_length=12)),
                ('cpf', models.CharField(max_length=12)),
                ('telefone', models.CharField(max_length=13)),
                ('cnh', models.CharField(max_length=12)),
                ('cnh_tipo', models.CharField(choices=[('Não Possui', 'Não Possui'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='Não Possui', max_length=12)),
                ('sexo_choices', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=2)),
                ('foto_colaborador', models.BinaryField(editable=True)),
            ],
            options={
                'db_table': 'Colaborador',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDepartamento', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Departamento',
            },
        ),
        migrations.CreateModel(
            name='TipoFormacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_formacao', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'Tipo_Formacao',
            },
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeFuncao', models.CharField(max_length=20)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ColaboraApp.Departamento')),
            ],
            options={
                'db_table': 'Funcao',
            },
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=50)),
                ('instituicao', models.CharField(max_length=50)),
                ('dt_inicio', models.DateField()),
                ('dt_termino', models.DateField()),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ColaboraApp.Colaborador')),
                ('tipo_formacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ColaboraApp.TipoFormacao')),
            ],
            options={
                'db_table': 'Formacao',
            },
        ),
        migrations.AddField(
            model_name='colaborador',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ColaboraApp.Departamento'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='funcao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ColaboraApp.Funcao'),
        ),
    ]
