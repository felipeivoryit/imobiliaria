from django.contrib import admin
from django import forms
from django.forms import ModelForm
from django.forms.utils import ErrorList

from .models import Configuracao, Finalidade, Tipo, Cidade, Bairro, Imovel, Status, Imagem

# Alterando títudo template admin
admin.site.site_header = 'Imobiliária'


# Personalizar admin model Configuracao
class ConfiguracaoAdmin(admin.ModelAdmin):

    # Elementos na tabela
    list_display = [
        'razao_social'
    ]
    empty_value_display = 'Não informado'

    # Limitando o cadastro de configuração a um objeto apenas
    def has_add_permission(self, request, obj=None):
        if Configuracao.objects.count() > 0:
            return False
        return True

# Personalizar admin model Finalidade
class FinalidadeAdmin(admin.ModelAdmin):

    # Elementos na tabela
    list_display = [
        'nome'
    ]
    empty_value_display = 'Não informado'

# Personalizar admin model Tipo
class TipoAdmin(admin.ModelAdmin):

    # Elementos na tabela
    list_display = [
        'nome'
    ]
    empty_value_display = 'Não informado'

# Adicionando tabela de imagens para serem cadastradas no imovel
class ImagensInstanceInline(admin.TabularInline):
    model = Imagem
class ImagemAdmin(admin.ModelAdmin):
    inlines = [ImagensInstanceInline,]

# Personalizar admin model Imovel
class ImovelAdmin(admin.ModelAdmin):
    inlines = [ImagensInstanceInline,]
    exclude = ('imagens',)
    list_display = [
        'pk',
        'cidade',
        'bairro',
        'descricao_resumida'
    ]
    empty_value_display = 'Não informado'

# Personalizar admin model Bairros
class BairroAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'cidade'
    ]


# Adicionando models a class admin

# Configurações
admin.site.register(Configuracao, ConfiguracaoAdmin)
# Finalidades
admin.site.register(Finalidade, FinalidadeAdmin)
# Tipos
admin.site.register(Tipo, TipoAdmin)
# Cidades
admin.site.register(Cidade)
# Bairros
admin.site.register(Bairro, BairroAdmin)
# Imóvel
admin.site.register(Imovel, ImovelAdmin)
# Status
admin.site.register(Status)
