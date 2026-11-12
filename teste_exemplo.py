#FUNÇÕES DE TESTES COM FIXTURES
from exemplo import adcionar_item


def test_adicionar_item_na_lista(compras):
    adcionar_item(Lista_compras, " Acucar", 5.50)
    assert len