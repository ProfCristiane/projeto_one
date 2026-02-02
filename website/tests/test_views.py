import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from website.models import Produto

# Obtém o model de usuário customizado
User = get_user_model()

# Garante acesso ao banco em todos os testes do arquivo
pytestmark = pytest.mark.django_db


def test_admin_consegue_cadastrar_produto(client):
    """
    ADMIN autenticado deve conseguir cadastrar produto
    e ser redirecionado para a listagem.
    """
    admin = User.objects.create_user(
        username='admin',
        password='123456',
        tipo='ADMIN'
    )

    client.login(username='admin', password='123456')

    response = client.post(
        reverse('produtos:cadastrar'),
        {
            'nome': 'Notebook',
            'categoria': 'computador',
            'quantidade': 5,
            'preco': 3500.00
        }
    )

    assert response.status_code == 302
    assert response.url == reverse('produtos:listar')
    assert Produto.objects.count() == 1

    produto = Produto.objects.first()
    assert produto.cadastrado_por == admin


def test_usuario_nao_admin_nao_pode_cadastrar_produto(client):
    """
    Usuário autenticado, mas sem perfil ADMIN,
    deve receber 403 Forbidden.
    """
    usuario = User.objects.create_user(
        username='cliente',
        password='123456',
        tipo='CLIENTE'
    )

    client.login(username='cliente', password='123456')

    response = client.post(
        reverse('produtos:cadastrar'),
        {
            'nome': 'Mouse',
            'categoria': 'acessorio',
            'quantidade': 3,
            'preco': 120.00
        }
    )

    assert response.status_code == 403
    assert Produto.objects.count() == 0


def test_usuario_nao_autenticado_e_redirecionado_para_login(client):
    """
    Usuário não autenticado deve ser redirecionado
    para a página de login.
    """
    response = client.get(reverse('produtos:cadastrar'))

    assert response.status_code == 302
    assert '/login/' in response.url
