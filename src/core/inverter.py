# src/core/inverter.py

def inverter_string(s: str) -> str:
    """
    Inverte a ordem dos caracteres de uma string sem utilizar funções prontas de inversão.

    Parâmetros:
        s (str): A string a ser invertida.

    Retorna:
        str: A string invertida.
    """
    caracteres = list(s)
    inicio, fim = 0, len(caracteres) - 1

    while inicio < fim:
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        inicio += 1
        fim -= 1

    return ''.join(caracteres)
