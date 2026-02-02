from django import forms
from django.forms import ModelForm
from .models import Cliente

class InsereClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'e_mail']
    