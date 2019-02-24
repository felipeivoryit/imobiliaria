from django.db import models

class Status(models.Model):
    tipo = models.CharField(
        max_length = 80,
        verbose_name = 'Status',
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
        return self.tipo

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
