from django.views.generic import ListView
from django.shortcuts import render
from django.core.serializers import serialize

from ..models import Configuracao
from ..models import Imovel
from ..models import Imagem
from ..models import Finalidade, Tipo
from ..models import Cidade


def view_home(request):

    # Retornar configurações
    configuracoes = Configuracao.objects.first()

    # Retornar finalidades cadastradas
    finalidades = Finalidade.objects.all()

    # Retornar tipos cadastrados
    tipos = Tipo.objects.all()

    # Retornar todos imoveis cadastrados
    imoveis = Imovel.objects.all()

    # Retornar todas as cidades cadastradas
    cidades = Cidade.objects.all()

    # Adicionando imagens de cada imóveis
    for imovel in imoveis:
        imovel.imagens = Imagem.objects.filter(imovel = imovel.pk)
        print(imovel.imagens)

    # Adicionando objeto para ser adicionado ao template
    contexto = {
        'configuracoes': configuracoes,
        'finalidades': finalidades,
        'tipos': tipos,
        'imoveis': imoveis,
        'cidades': cidades
        #'imoveis': serialize('json', imoveis)
    }

    # Retornar dados para o template
    return render(
        request,
        'home.html',
        contexto
    )
