from django.urls import path, include
from clientes.views import ClientesListView, ClientesCreateView

app_name = 'clientes'

urlpatterns = [
    path('listar/', ClientesListView.as_view(), name='listar'),
    path('cadastrar/', ClientesCreateView.as_view(), name='cadastrar'),

]