import pytest
from datetime import datetime
from src.contrato import Vendas


# Testes com dados validos, cahma mocar os dados
def test_vendas_com_dados():
    dados_validos = {
        'email': 'comprador@example.com',
        'data': datetime.now(),
        'valor': 100.50,
        'produto': 'produto X',
        'quantidade': 3,
        'categoria': 'categoria3',


    }

    # A sintaxe **dados_validos é uma forma de desempacotarmento de dicionários em Python.
    # O que isso faz é passar os pares chave-valor no dicionário daos_validos como argumentos nomeados para 

    venda = Vendas(**dados_validos)
    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]
