from django.db import models

class Finalidade(models.Model):
    nome = models.CharField(
        max_length = 100,
        verbose_name = 'Finalidade',
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
        verbose_name = 'Finalidade'
        verbose_name_plural = 'Finalidades'
