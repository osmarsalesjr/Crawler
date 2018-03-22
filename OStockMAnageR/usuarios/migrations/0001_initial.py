# Generated by Django 2.0 on 2018-03-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('nome_empresa', models.CharField(max_length=255)),
                ('email_empresa', models.EmailField(max_length=255)),
                ('telefone_empresa', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome_funcionario', models.CharField(max_length=255)),
                ('email_funcionario', models.EmailField(max_length=255)),
                ('telefone_funcionario', models.CharField(max_length=255)),
                ('empresa_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to='usuarios.Empresa')),
            ],
        ),
    ]