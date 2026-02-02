from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from clientes.models import Cliente
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InsereClienteForm


class ClientesListView(LoginRequiredMixin, ListView):
    template_name = "clientes.html"
    model = Cliente
    context_object_name = "clientes"

class ClientesCreateView(LoginRequiredMixin, CreateView):
    template_name = "cliente_form.html"
    model = Cliente
    form_class = InsereClienteForm
    success_url = reverse_lazy("clientes:listar")
    
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.tipo != 'ADMIN':
            return HttpResponseForbidden("Você não tem permissão para cadastrar clientes.")
        return super().dispatch(request, *args, **kwargs)