# Funções para testar (podem estar no seu main.py ou aqui mesmo para facilitar)
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

# Os 5 testes unitários exigidos
def test_soma_positiva():
    assert soma(2, 2) == 4

def test_soma_negativa():
    assert soma(-1, -1) == -2

def test_subtracao_comum():
    assert subtracao(10, 5) == 5

def test_soma_zero():
    assert soma(10, 0) == 10

def test_tipo_retorno():
    assert isinstance(soma(1, 1), int)
