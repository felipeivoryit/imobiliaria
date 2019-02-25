from django.db import models

from . import Status
from . import Finalidade
from . import Tipo
from . import Cidade
from . import Bairro

from smart_selects.db_fields import ChainedForeignKey


class Imovel(models.Model):

    status = models.ForeignKey(
        Status, on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    descricao = models.TextField(
        max_length = 200,
        verbose_name = 'Descrição',
        null = True,
        blank = True
    )
    descricao_resumida = models.TextField(
        max_length = 80,
        verbose_name = 'Decrição resumida',
        null = True,
        blank = True
    )
    valor = models.CharField(
        max_length = 60,
        verbose_name = 'Valor',
        null = True,
        blank = True
    )
    quarto = models.IntegerField(
        verbose_name = 'Quarto',
        default = 0
    )
    bainheiro = models.IntegerField(
        verbose_name = 'Bainheiro',
        default = 0
    )
    vaga = models.IntegerField(
        verbose_name = 'Vaga',
        default = 0
    )
    area = models.FloatField(
        verbose_name = 'Area',
        default = 0
    )

    # Chaves estrangeiras
    finalidade = models.ForeignKey(
        Finalidade, on_delete = models.CASCADE
    )
    tipo = models.ForeignKey(
        Tipo, on_delete = models.CASCADE
    )
    cidade = models.ForeignKey(
        Cidade, on_delete = models.CASCADE
    )
    bairro = ChainedForeignKey(
        Bairro,
        chained_field="cidade",
        chained_model_field="cidade",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Criado'
    )
    update_at = models.DateTimeField(
        auto_now = True,
        verbose_name = 'Atualizado'
    )

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
