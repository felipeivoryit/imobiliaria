from django.db import models

from . import Cidade

class Bairro(models.Model):
    nome = models.CharField(
        max_length = 120,
        verbose_name = 'Bairro',
        unique = True
    )
    cidade = models.ForeignKey(
        Cidade, on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Criado'
    )
    update_at = models.DateTimeField(
        auto_now = True,
        verbose_name = 'Atualizado'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'
