from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from website.models import Produto
from django.views.generic import ListView
from .forms import ContatoForm, ProdutoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    #return HttpResponse("Olá, Django!")
    return render(request, "website/base.html")

@login_required
def produtos(request):
    lista_produtos = Produto.objects.all()
    contexto = {'produtos': lista_produtos}
    return render(request, "website/produtos.html", contexto)


class ProdutosListView(LoginRequiredMixin, ListView):
    template_name = "website/produtos.html"
    model = Produto
    context_object_name = "produtos"

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form = ContatoForm()  
    else:
        form = ContatoForm()

    return render(request, 'website/contato.html', {'form': form})

@login_required
def cadastrar_produto(request):
    if request.user.tipo != 'ADMIN':
        return HttpResponseForbidden('Apenas administradores podem cadastrar produtos')

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.cadastrado_por = request.user
            produto.save()
            return redirect('produtos:listar')
    else:
        form = ProdutoForm()
    return render(request, 'website/produto_form.html', {'form': form})