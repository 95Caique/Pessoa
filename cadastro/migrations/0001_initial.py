# Generated by Django 5.1.3 on 2024-12-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]