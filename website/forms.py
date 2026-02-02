from django import forms
from django.forms import ModelForm
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(
    label="Nome completo",
    max_length=100,
    required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Informe seu nome completo'})
    #help_text="Informe seu nome completo" 
    )
    email = forms.EmailField(
    label="E-mail",
    required=True
    )
    mensagem = forms.CharField(
    label="Mensagem",
    widget=forms.Textarea(attrs={'rows': 4}),
    required=True
    )

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'quantidade', 'preco']
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError('A quantidade não pode ser negativo, nem igual a zero.')
        return quantidade