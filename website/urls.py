from django.urls import path, include
from .views import home, contato, cadastrar_produto
from website.views import ProdutosListView


app_name = 'produtos'

urlpatterns = [
    
    path('', home, name='home'),
    path('listar/', ProdutosListView.as_view(), name='listar'),
    path('faleconosco/', contato, name='contato'),
    path('cadastrar/', cadastrar_produto, name='cadastrar'),
    
]
