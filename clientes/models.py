from django.db import models
from django.conf import settings

class Cliente(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=100)
    e_mail = models.CharField(max_length=50)
    cadastrado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf
