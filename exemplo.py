
        raise ValueError("O valor do pagamento de ve ser positivo.")
    if valor > saldo:#FUNÇÕES PARA TESTES COM FIXTURES
#FUNÇÃO PARA CADASTRAR ITEM
def adcionar_item(lista, item, preco):
    if not item.strip():
       raise ValueError("O nome do item não pode ser vazio.") 
    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

    produto = {
        "nome": item,
        "preco": preco
    }
    lista.append(produto)
    return produto

#FUNÇÃO PARA CALCULAR O TOTAL DE ITENS
def calcular_total(lista):
    return round(sum(item["preco"] for item in lista), 2)

#FUNÇÃO PARA APLICAR O PAGAMENTO 
def aplicar_pagamento(saldo, valor):
    if valor <= 0:
        raise ValueError("saldo insufuciente")
    return saldo - valor
#FUNÇÃO PARA FILTRAR ITEM POR PRECO 
def filtrar_por_preco(lista,limite):
    return[
        item for item in lista
        if item["preco"] <= limite
    ]

