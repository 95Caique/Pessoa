from django.contrib import admin
from .models import PessoaFisica

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'data_nascimento')