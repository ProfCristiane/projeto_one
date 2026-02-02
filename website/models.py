from django.db import models
from django.core.exceptions import ValidationError
from principal.settings import AUTH_USER_MODEL

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    cadastrado_por = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def clean(self):
        if self.quantidade < 0:
            raise ValidationError("Quantidade inválida")

