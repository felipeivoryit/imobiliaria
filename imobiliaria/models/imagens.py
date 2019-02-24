from django.db import models

from . import Imovel


class Imagem(models.Model):

    imovel = models.ForeignKey(
        Imovel,
        on_delete = models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to = 'imovel/images',
        verbose_name = 'Imagem'
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
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
