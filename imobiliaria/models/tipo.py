from django.db import models

class Tipo(models.Model):
    nome = models.CharField(
        max_length = 80,
        verbose_name = 'Tipo',
        unique = True
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
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
