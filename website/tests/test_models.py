import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from website.models import Produto

User = get_user_model()
pytestmark = pytest.mark.django_db


def test_criar_produto():
    usuario = User.objects.create_user(
        username='admin',
        password='123456'
    )

    produto = Produto.objects.create(
        nome="Teclado Mecânico",
        categoria="acessorio",
        quantidade=10,
        preco=250.00,
        cadastrado_por=usuario
    )

    assert produto.id is not None
    assert produto.nome == "Teclado Mecânico"
    assert produto.quantidade == 10


def test_produto_nao_pode_ter_quantidade_negativa():
    usuario = User.objects.create_user(
        username='admin2',
        password='123456'
    )

    produto = Produto(
        nome="Mouse",
        categoria="acessorio",
        quantidade=-1,
        preco=100.00,
        cadastrado_por=usuario
    )

    with pytest.raises(ValidationError):
        produto.full_clean()
