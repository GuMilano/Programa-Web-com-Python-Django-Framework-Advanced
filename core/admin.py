from django.contrib import admin

from .models import Cargo, Funcionario, Servico

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'criados', 'modificado')
    list_filter = ('ativo',)
    search_fields = ('cargo',)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'criados', 'modificado')
    list_filter = ('cargo', 'ativo',)
    search_fields = ('nome',)

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'criados', 'modificado')
    list_filter = ('ativo',)
    search_fields = ('servico',)