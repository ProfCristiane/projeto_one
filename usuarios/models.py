from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('VENDEDOR', 'Vendedor'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
