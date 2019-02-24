from django.views.generic import ListView
from django.shortcuts import render
from django.core.serializers import serialize

from ..models import Configuracao
from ..models import Imovel
from ..models import Imagem


def view_home(request):

    # Retornar configurações
    configuracoes = Configuracao.objects.first()

    # Retornar todos imoveis cadastrados
    imoveis = Imovel.objects.all()

    for imovel in imoveis:
        imovel.imagens = Imagem.objects.filter(imovel = imovel.pk)
        print(imovel.imagens)

    # Adicionando objeto para ser adicionado ao template
    contexto = {
        'configuracoes': configuracoes,
        'imoveis': imoveis
        #'imoveis': serialize('json', imoveis)
    }

    # Retornar dados para o template
    return render(
        request,
        'home.html',
        contexto
    )
