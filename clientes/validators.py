import re

def cpf_valido(numero_do_cpf):
    return len(numero_do_cpf) == 11

def nome_valido(nome):
    return all(caracter.isalpha() or caracter.isspace() for caracter in nome)


def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(celular):
    """Verifica se o celular é valido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta

