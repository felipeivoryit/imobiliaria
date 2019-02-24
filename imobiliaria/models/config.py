from __future__ import unicode_literals

from django.db import models

# === Model configuração, dados referentes a imobiliaria ===

class Configuracao(models.Model):
    razao_social = models.CharField(
        max_length=100,
        verbose_name = 'Razão Social',
    )
    logo_tipo = models.ImageField(
        upload_to = 'config/images',
        verbose_name = 'Logo tipo',
        blank = True,
        null = True,
    )
    # Contatos
    telefone = models.EmailField(
        max_length=15,
        verbose_name = 'Telefone',
        blank=True,
        null=True
    )
    celular = models.EmailField(
        max_length=16,
        verbose_name = 'Celular',
        blank=True,
        null=True
    )
    email = models.EmailField(
        max_length=40,
        verbose_name = 'E-mail',
        blank=True,
        null=True
    )
    endereco = models.TextField(
        verbose_name = 'Endereço',
        blank = True,
        null = True,
    )

    # Cabeçalho
    titulo = models.CharField(
        max_length=60,
        verbose_name = 'Título',
        blank=True,
        null=True
    )
    # Limitar três imagens
    image = models.ImageField(
        upload_to = 'config/images',
        verbose_name = 'Imagem 1',
        blank = True,
        null = True,
    )
    image2 = models.ImageField(
        upload_to = 'config/images',
        verbose_name = 'Imagem 2',
        blank = True,
        null = True,
    )
    image3 = models.ImageField(
        upload_to = 'config/images',
        verbose_name = 'Imagem 3',
        blank = True,
        null = True,
    )
    sobre = models.TextField(
        verbose_name = 'Sobre nós',
        blank = True,
        null = True,
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
        return self.razao_social

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'
